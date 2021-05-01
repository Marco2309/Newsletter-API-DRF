from rest_framework.test import APITestCase
from newsletter_app.models import Newsletters
from tags_app.models import Tag
from django.contrib.auth.models import User, Group

class TestNewsLetter(APITestCase):
    
    def setUp(self):
        self.host = 'http://127.0.0.1:8000'
        self.tag = Tag.objects.create(
            nombre = 'tag 1',
            slug = 'slug 1',
            fecha_creacion = '2021-04-27'
        )
        self.groups_admin = Group.objects.create(
            name = 'administrador'
        )
        self.groups_usuario = Group.objects.create(
            name = 'usuario'
        )
        self.user = User.objects.create_user(
            username='user',
            email = 'prueba@mail.com',
            password = 'test',
        )
        self.user.groups.add(self.groups_admin)
        response = self.client.post(f'{self.host}/api/token/',{
            'username': 'user',
            'password': 'test'
        })
        self.auth = f'Bearer {response.data["access"]}'
        
        self.newsletter = Newsletters.objects.create(
            nombre = 'newsletter 1',
            description = 'description 1 ',
            target = 1,
            frecuencia = 'frecuencia 1',
            fecha_creacion = '2020-04-06',
        )
        self.newsletter.tags.add(self.tag)
        self.newsletter.users.add(self.user)
        self.newsletter.members.add(self.user)
        self.newsletter.voters.add(self.user)
        
    def test_get_newsletter(self):
        response = self.client.get(f'{self.host}/newsletter/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Newsletters.objects.all().count(), 1)
        self.assertEqual(len(response.data), 1)
    
    def test_post_newsletter(self):
        data={
            'nombre' : 'newsletter 2',
            'description' : 'description 2',
            'target': 2,
            'frecuencia' : 'frecuencia 2',
            'tags' : [self.tag.id],
            'fecha_creacion' : '2020-04-06',
            'user': self.user.id,
            'users': [self.user.id],
            'members': [self.user.id],
            'voters': [self.user.id]
        }
        response = self.client.post(f'{self.host}/newsletter/', data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(Newsletters.objects.all().count(), 2)
        self.assertEqual(Newsletters.objects.get(id=self.newsletter.id).nombre, 'newsletter 1')
        
    
    def test_put_newsletter(self):
        data = {
            'nombre' : 'newsletter actualizado',
            'description' : 'description actualizado',
            'target': 1,
            'frecuencia' : 'frecuencia actualizado',
            'tags' : [self.tag.id],
            'fecha_creacion' : '2020-04-06',
            'user': self.user.id,
            'users': [self.user.id],
            'members': [self.user.id],
            'voters': [self.user.id]
        }
        nombre_newsletter = Newsletters.objects.get(id=self.newsletter.id).nombre
        response = self.client.put(f'{self.host}/newsletter/{self.newsletter.id}/',data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, 200, response.data)
        self.assertNotEqual(nombre_newsletter, data['nombre'])
        
    def test_delete_newsletter(self):
        response = self.client.delete(f'{self.host}/newsletter/{self.newsletter.id}/', HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(Newsletters.objects.all()), 0)