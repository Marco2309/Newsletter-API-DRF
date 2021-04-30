from rest_framework.test import APITestCase

from users_app.models import User


class TestLoginRegister(APITestCase):
    def setUp(self):
        self.host = 'http://127.0.0.1:8000'
        self.user = User.objects.create(
            username= 'user1',
            password= 'password1234',
            email= 'email@gmail.com',
            first_name= 'John',
            last_name= 'Doe'
        )

    def test_register_user(self):
        data = {
            'username': 'user2',
            'password': 'password1234',
            'email': 'email@gmail.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        response = self.client.post(f'{self.host}/user/', data)

        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(User.objects.all().count(), 2)

    def test_register_admin(self):
        data = {
            'username': 'admin1',
            'password': 'password1234',
            'email': 'email@gmail.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        response = self.client.post(f'{self.host}/user/admin/', data)

        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(User.objects.all().count(), 2)

    def test_login_user(self):
        data = {
            'username': 'user1',
            'password': 'password1234',
        }
        response = self.client.post(f'{self.host}/api/token/', data)

        self.assertEqual(response.status_code, 200, response.data)

    def test_login_admin(self):
        data = {
            'username': 'user1',
            'password': 'password1234',
        }
        response = self.client.post(f'{self.host}/api/token/', data)

        self.assertEqual(response.status_code, 200, response.data)
