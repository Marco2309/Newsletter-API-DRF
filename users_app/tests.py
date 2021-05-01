from rest_framework.test import APITestCase

from django.contrib.auth.models import User, Group


class TestLoginRegister(APITestCase):
    def setUp(self):
        self.host = 'http://127.0.0.1:8000'
        self.groups_admin = Group.objects.create(
            name='administrador'
        )
        self.groups_usuario = Group.objects.create(
            name='usuario'
        )
        self.user = User.objects.create_user(
            username='user',
            email='user@mail.com',
            password='test',
        )
        self.user.groups.add(self.groups_usuario)
        self.admin = User.objects.create_user(
            username='admin',
            email='admin@mail.com',
            password='test',
        )
        self.admin.groups.add(self.groups_admin)

    def test_login_user(self):
        response = self.client.post(f'{self.host}/api/token/', {
            'username': 'user',
            'password': 'test'
        })
        self.auth = f'Bearer {response.data["access"]}'
        self.assertEqual(response.status_code, 200)

    def test_login_admin(self):
        response = self.client.post(f'{self.host}/api/token/', {
            'username': 'admin',
            'password': 'test'
        })
        self.auth = f'Bearer {response.data["access"]}'
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        data = {
            'username': 'user2',
            'password': 'password1234',
            'email': 'email@gmail.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        response = self.client.post(f'http://127.0.0.1:8000/user/', data)

        self.assertEqual(response.status_code, 201, response.data)

    def test_register_admin(self):
        data = {
            'username': 'admin2',
            'password': 'password1234',
            'email': 'email@gmail.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        response = self.client.post(f'http://127.0.0.1:8000/user/admin/', data)

        self.assertEqual(response.status_code, 201, response.data)
