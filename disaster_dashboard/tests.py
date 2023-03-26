from django.test import Client, TestCase
from .models import DisasterList

class ViewTestCase(TestCase):
    def test_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

