from django.shortcuts import render
from .models import summary as DisList
import sqlite3
from django.db import connection
# Create your views here.
# use f-strings for easy string formatting https://realpython.com/python-f-strings/ 

def index(request, show_id):
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM disaster_table_summary AS a LEFT JOIN disaster_table_details AS b ON a.id = b.Dis_ID_id WHERE a.Dis_ID = ?', (show_id,))
    myList = cursor.fetchall()
    # print(myList) # Check how the data show
    connection.close()
    return render(request, 'disaster_edit/index.html', {'list': myList})

# def get_myList():
#     disasters = DisasterList.objects
#     return disasters