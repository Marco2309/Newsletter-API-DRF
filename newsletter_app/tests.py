# import os
# import io

from rest_framework.test import APITestCase
from newsletter_app.models import Newsletters
from tags_app.models import Tag
from users_app.models import User
from rest_framework.test import force_authenticate
# from PIL import Image

class TestNewsLetter(APITestCase):
    
    def setUp(self):
        
        # super().setUp()
        # self.newsletter.imagen = tempfile.NamedTemporaryFile(suffix='.jpg')
        # image = Image.new('RGB', (100, 100))
        # image.save(self.newsletter.imagen.name)
        # self.params = {
        #     'photo': self.newsletter.imagen
        # }
        
        self.host = 'http://127.0.0.1:8000'
        self.tag = Tag.objects.create(
            nombre = 'tag 1',
            slug = 'slug 1',
            fecha_creacion = '2021-04-27'
        )
        self.user1 = User.objects.create(
            is_administrador = True,
            username='prueba 1',
            password = '12345',
            email = 'prueba@mail.com',
            first_name = 'prueba',
            last_name = 'prueba'
        )
        self.newsletter = Newsletters.objects.create(
            nombre = 'newsletter 1',
            description = 'description 1 ',
            target = 1,
            frecuencia = 'frecuencia 1',
            fecha_creacion = '2020-04-06'
        )
        self.newsletter.tags.add(self.tag)
        
    def test_get_newsletter(self):
        response = self.client.get(f'{self.host}/newsletter/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Newsletters.objects.all().count(), 1)
        self.assertEqual(len(response.data), 1)
        
    
    # def test_valid_authenticated_post_returns_201(self):
    #     response = self.auth_client.post(
    #         reverse(self.view_name), data=self.params, format='multipart')
    
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    
    
    def test_post_newsletter(self):
        data = {
            'nombre' : 'newsletter 2',
            'description' : 'description 2',
            # 'imagen' : self.generate_photo_file(),
            'target': 2,
            'frecuencia' : 'frecuencia 2',
            'tags' : [self.tag.id],
            'fecha_creacion' : '2020-04-06',
            'user': self.user1.id
        }
        response = self.client.post(f'{self.host}/newsletter/', data, format='json')
        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(Newsletters.objects.all().count(), 2)
        self.assertEqual(Newsletters.objects.get(id=1).nombre, 'newsletter 1')
        # print(response.data)
        self.assertEqual(len(response.data), 11)
    
    def test_post_logIn_authenticated(self):
        data = {
            'nombre' : 'newsletter 3',
            'description' : 'description 3',
            'target': 3,
            'frecuencia' : 'frecuencia 3',
            'tags' : [self.tag.id],
            'fecha_creacion' : '2020-04-06',
            'user': self.user1.id
        }
        self.client.force_authenticate(self.user1)
        response = self.client.post(f'{self.host}/newsletter/', data)
        self.assertEqual(response.status_code, 201)
        
    
    def test_put_newsletter(self):
        data = {
            'nombre' : 'newsletter actualizado',
            'description' : 'description actualizado',
            'target': 1,
            'frecuencia' : 'frecuencia actualizado',
            'tags' : [self.tag.id],
            'fecha_creacion' : '2020-04-06',
            'user': self.user1.id
        }
        nombre_newsletter = Newsletters.objects.get(id=self.newsletter.id).nombre
        response = self.client.put(f'{self.host}/newsletter/{self.newsletter.id}/',data)
        self.assertEqual(response.status_code, 200, response.data)
        self.assertNotEqual(nombre_newsletter, data['nombre'])
        
    def test_delete_newsletter(self):
        response = self.client.delete(f'{self.host}/newsletter/{self.newsletter.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(Newsletters.objects.all()), 0)