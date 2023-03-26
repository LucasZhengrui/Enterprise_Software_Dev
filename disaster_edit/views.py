from django.shortcuts import render
from .models import summary as DisList
import sqlite3
from django.db import connection
from .models import Message
# Create your views here.
# use f-strings for easy string formatting https://realpython.com/python-f-strings/ 

def get_message_obj():
    message_obj = Message.objects.order_by('-id')
    return message_obj

def index(request, show_id):
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM disaster_table_summary AS a LEFT JOIN disaster_table_details AS b ON a.id = b.Dis_ID_id WHERE a.id = ?', (show_id,))
    myList = cursor.fetchall()
    message_obj = get_message_obj()
    connection.close()
    return render(request, 'disaster_edit/index.html', {'list': myList, 'message_obj': message_obj})