from django.test import Client, TestCase
from .models import summary as DisasterList

class ViewTestCase(TestCase):
    def setUp(self):
        DisasterList.objects.create(Dis_ID=1, Year=2010, Disaster_Group='Disaster Group 1',
                                    Disaster_Type='Disaster Type 1', Country='Country 1',
                                    ISO='ISO 1', Total_Affected=1000, Total_Damages=10000)
        DisasterList.objects.create(Dis_ID=2, Year=2011, Disaster_Group='Disaster Group 2',
                                    Disaster_Type='Disaster Type 2', Country='Country 2',
                                    ISO='ISO 2', Total_Affected=2000, Total_Damages=20000)
        DisasterList.objects.create(Dis_ID=3, Year=2012, Disaster_Group='Disaster Group 3',
                                    Disaster_Type='Disaster Type 3', Country='Country 3',
                                    ISO='ISO 3', Total_Affected=3000, Total_Damages=30000)

    def test_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'disaster_list/index.html')
        self.assertContains(response, 'Disaster Group 1')
        self.assertContains(response, 'Disaster Group 2')
        self.assertContains(response, 'Disaster Group 3')

    def test_search(self):
        client = Client()
        response = client.get('/search/?search_query=2010&search_field=Year')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'disaster_list/index.html')
        self.assertContains(response, 'Disaster Group 1')
        self.assertNotContains(response, 'Disaster Group 2')
        self.assertNotContains(response, 'Disaster Group 3')

    def test_delete(self):
        client = Client()
        response = client.get('/delete/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'disaster_list/index.html')
        self.assertNotContains(response, 'Disaster Group 1')
