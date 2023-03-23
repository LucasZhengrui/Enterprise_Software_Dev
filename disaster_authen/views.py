from django.shortcuts import render
from django.contrib import messages
from .models import DisasterUser
import hashlib
from django.http import HttpResponseRedirect
from django.http import HttpResponse


# Create your views here.
# use f-strings for easy string formatting https://realpython.com/python-f-strings/ 
def index(request):
    return render(request, 'disaster_authen/index.html')

def goto_index_view(request):
    # 重定向到 example.com
    return HttpResponseRedirect('/list')


def login(request):
    if request.method == 'POST':
        # 获取用户输入的用户名和密码
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 在数据库中查找用户
        try:
            user = DisasterUser.objects.get(user_name=username, is_delete=0)
        except DisasterUser.DoesNotExist:
            error_message = 'Invalid username or password'
            return render(request, 'disaster_authen/login.html', {'error_message': error_message})

        # 检查密码是否匹配
        password_md5 = hashlib.md5(password.encode('utf-8')).hexdigest()
        if password_md5 != user.user_password:
            error_message = 'Username or password does not match'
            return render(request, 'disaster_authen/login.html', {'error_message': error_message})

        # 检查用户是否被禁用
        if user.is_banned:
            error_message = 'Your account has been banned'
            return render(request, 'disaster_authen/login.html', {'error_message': error_message})

        # 将用户登录状态设置为 "已登录"
        user.login_status = 1
        user.save()

        # 创建响应对象并设置 cookie
        response = goto_index_view(request)
        response.set_cookie('username', username)

        return response

    else:
         response = render(request, 'disaster_authen/login.html')
         response.delete_cookie('username')
         return response