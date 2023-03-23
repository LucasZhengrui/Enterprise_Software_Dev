from django.shortcuts import render
from .models import Message
from django.http import HttpResponseRedirect

# Create your views here.
# use f-strings for easy string formatting https://realpython.com/python-f-strings/ 


def get_message_obj(request):
    message_obj = Message.objects.order_by('-id')
    return message_obj

def index(request):
    message_obj = get_message_obj(request)
    return render(request, 'disaster_chat/index.html', {'message_obj': message_obj})


def message_submit(request):
    message = request.GET.get('message')
    if message:
        # create a new message instance
        new_message = Message(message=message)
        # save the message to the database
        new_message.save()
    
    return HttpResponseRedirect('/chat')