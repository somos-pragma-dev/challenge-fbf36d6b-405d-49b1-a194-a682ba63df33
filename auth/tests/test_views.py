from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

class UserCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('user-create')
        self.data = {'username': 'testuser', 'password': 'testpassword'}

    def test_create_user(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, 201)