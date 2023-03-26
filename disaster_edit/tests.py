from django.test import Client, TestCase
from .models import Message
import sqlite3

class DisasterEditTestCase(TestCase):
    def setUp(self):
        Message.objects.create(message="test message 1")
        Message.objects.create(message="test message 2")

def test_index_view(self):
    c = Client()
    response = c.get('/edit/1/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'disaster_edit/index.html')

    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM disaster_table_summary AS a LEFT JOIN disaster_table_details AS b ON a.id = b.Dis_ID_id WHERE a.id = 1')
    myList = cursor.fetchall()
    connection.close()

    self.assertEqual(response.context['list'], myList)
    self.assertEqual(len(response.context['message_obj']), 2)
