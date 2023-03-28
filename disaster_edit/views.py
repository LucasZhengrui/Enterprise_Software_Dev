from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
import sqlite3
from .models import Message, summary
from .forms import DataForm
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

def summary_edit(request, id):
    message_obj = get_message_obj()
    datamsg = get_object_or_404(summary, id=id)
    if request.method == "POST":
        form = DataForm(request.POST, instance=datamsg)
        if form.is_valid():
            datamsg = form.save(commit=False)
            # datamsg.created_date = timezone.now()
            datamsg.save()
            return redirect("/", id = datamsg.id)
    else:
        form = DataForm(instance=datamsg)
    return render(request, 'disaster_edit/edit.html', {'form': form, 'datamsg': datamsg, 'message_obj': message_obj})