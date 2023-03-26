from django.test import Client, TestCase
from .models import DisasterUser
import hashlib

class DisasterAuthenTestCase(TestCase):
    def setUp(self):
      DisasterUser.objects.create(user_name="testuser", user_password=hashlib.md5("testpassword".encode('utf-8')).hexdigest(), user_level=2, login_status=0, is_banned=0, is_delete=0, is_approved=1)

def test_login(self):
    c = Client()
    response = c.post('/authen/login/', {'username': 'testuser', 'password': 'testpassword'})
    self.assertEqual(response.status_code, 302)
    self.assertEqual(response.url, '/list')
    self.assertEqual(c.cookies.get('username').value, 'testuser')

def test_incorrect_login(self):
    c = Client()
    response = c.post('/authen/login/', {'username': 'testuser', 'password': 'incorrectpassword'})
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'disaster_authen/login.html')
    self.assertContains(response, 'Invalid username or password')

def test_add_user(self):
    c = Client()
    response = c.post('/authen/adduser/', {'username': 'newuser', 'password': 'newpassword', 'confirm_password': 'newpassword'})
    self.assertEqual(response.status_code, 302)
    self.assertEqual(response.url, '/authen/user/')
    user = DisasterUser.objects.get(user_name='newuser')
    self.assertEqual(user.user_name, 'newuser')

def test_incorrect_add_user(self):
    c = Client()
    response = c.post('/authen/adduser/', {'username': 'newuser', 'password': 'newpassword', 'confirm_password': 'incorrectpassword'})
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'disaster_authen/useradd.html')
    self.assertContains(response, 'Password is not the same as the confirmation password')

def test_remove_user(self):
    c = Client()
    user = DisasterUser.objects.get(user_name='testuser')
    response = c.get(f'/authen/remove/{user.user_id}/')
    self.assertEqual(response.status_code, 302)
    self.assertEqual(response.url, '/authen/user/')
    user = DisasterUser.objects.get(user_name='testuser')
    self.assertEqual(user.is_delete, 1)

def test_user_list(self):
    c = Client()
    response = c.get('/authen/user/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'disaster_authen/userlist.html')
