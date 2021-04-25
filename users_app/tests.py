from rest_framework.test import APITestCase

from users_app.models import User


class TestLoginRegister(APITestCase):
    def setUp(self):
        self.host = 'http://127.0.0.1:8000'

    def test_register_user(self):
        data = {
            'username': 'user1',
            'password': 'password1234',
            'email': 'email@gmail.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'is_administrador': False
        }
        response = self.client.post(f'{self.host}/user/', data)

        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(User.objects.all().count(), 1)

    def test_register_admin(self):
        data = {
            'username': 'admin1',
            'password': 'password1234',
            'email': 'email@gmail.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'is_administrador': True
        }
        response = self.client.post(f'{self.host}/user/admin/', data)

        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(User.objects.all().count(), 1)

    def test_login_user(self):
        data = {
            'username': 'user1',
            'password': 'password1234',
        }
        response = self.client.post(f'{self.host}/user/1', data)

        self.assertEqual(response.status_code, 302, response.data)
        self.assertEqual(User.objects.all().count(), 1)

    def test_login_admin(self):
        data = {
            'username': 'user1',
            'password': 'password1234',
        }
        response = self.client.post(f'{self.host}/user/admin/1', data)

        self.assertEqual(response.status_code, 302, response.data)
        self.assertEqual(User.objects.all().count(), 1)
