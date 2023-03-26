from django.test import Client, TestCase
from .models import DisasterList

class DisasterTrashListTestCase(TestCase):
    def setUp(self):
      DisasterList.objects.create(Dis_Name="Test Disaster", Dis_Type="Test Type", is_delete=1)

def test_recovery(self):
    c = Client()
    disaster = DisasterList.objects.get(Dis_Name="Test Disaster")
    response = c.get(f'/trash/recovery/{disaster.Dis_ID}/')
    self.assertEqual(response.status_code, 302)
    self.assertEqual(response.url, '/trash')
    disaster = DisasterList.objects.get(Dis_Name="Test Disaster")
    self.assertEqual(disaster.is_delete, 0)

def test_trash_list(self):
    c = Client()
    response = c.get('/trash/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'disaster_trash_list/index.html')
    self.assertContains(response, 'Test Disaster')
    self.assertContains(response, 'Test Type')
