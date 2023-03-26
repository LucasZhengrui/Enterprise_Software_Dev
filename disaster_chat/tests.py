from django.test import Client, TestCase
from .models import Message

class DisasterChatTestCase(TestCase):

    def test_index(self):
        c = Client()
        response = c.get('/chat/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'disaster_chat/index.html')

    def test_message_submit(self):
        c = Client()
        response = c.get('/chat/message_submit/', {'message': 'Hello World'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/chat')
        message = Message.objects.get(message='Hello World')
        self.assertEqual(message.message, 'Hello World')
