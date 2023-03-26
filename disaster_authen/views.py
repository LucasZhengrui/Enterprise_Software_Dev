from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from .models import DisasterUser
import hashlib
import sqlite3
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Message


def get_message_obj():
    message_obj = Message.objects.order_by('-id')
    return message_obj

def index(request):
    return render(request, 'disaster_authen/index.html')

def goto_index_view(request,url):
    # Redirect to example.com
    return HttpResponseRedirect(url)


def login(request):
    if request.method == 'POST':
        # Get the user name and password entered by the user
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Find a user in the database
        try:
            user = DisasterUser.objects.get(user_name=username, is_delete=0)
        except DisasterUser.DoesNotExist:
            error_message = 'Invalid username or password'
            return render(request, 'disaster_authen/login.html', {'error_message': error_message})

        # Check if the password matches
        password_md5 = hashlib.md5(password.encode('utf-8')).hexdigest()
        if password_md5 != user.user_password:
            error_message = 'Username or password does not match'
            return render(request, 'disaster_authen/login.html', {'error_message': error_message})

        # Check if the user is disabled
        if user.is_banned:
            error_message = 'Your account has been banned'
            return render(request, 'disaster_authen/login.html', {'error_message': error_message})

        # Set user login status to "logged in"
        user.login_status = 1
        user.save()

        # Create a response object and set a cookie
        response = goto_index_view(request,'/list')
        response.set_cookie('username', username)

        return response

    else:
        response = render(request, 'disaster_authen/login.html')
        username = request.COOKIES.get('username')
        try:
            user = DisasterUser.objects.get(user_name=username, is_delete=0)
            user.login_status = 0
            user.save()
        except DisasterUser.DoesNotExist:
            pass
        
        response.delete_cookie('username')
        return response


def user_list(request):
    message_obj = get_message_obj()
    users = DisasterUser.objects.filter(is_delete=0)

    return render(request, 'disaster_authen/userlist.html', {'users': users,'message_obj': message_obj})



def add_user(request):
    err_message = ""
    if request.method == 'POST':
        # get user input data from request.POST
        user_password = request.POST.get('password')
        user_confirm_password = request.POST.get('confirm_password')
        
        if user_password != user_confirm_password:
              err_message = "Password is not the same as the confirmation password"
              return render(request, 'disaster_authen/useradd.html',{'err_message':err_message})
        
        password_md5 = hashlib.md5(user_password.encode('utf-8')).hexdigest()
        user_name = request.POST.get('username')
        user_level = 2
        login_status = 0
        is_banned = 0
        is_delete = 0
        is_approved = 1

        # create a new user record in the database
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        query = "INSERT INTO disaster_user (user_password, user_name, user_level, login_status, is_banned, is_delete, is_approved) VALUES (?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (password_md5, user_name, user_level, login_status, is_banned, is_delete, is_approved))
        conn.commit()
        conn.close()

        response = goto_index_view(request,'/authen/user/')
        return response
    else:
        return render(request, 'disaster_authen/useradd.html')

def remove_user(request,user_id):
    disaster = DisasterUser.objects.get(user_id=user_id)
    disaster.is_delete = 1
    disaster.save()
    response = goto_index_view(request,'/authen/user/')
    return response