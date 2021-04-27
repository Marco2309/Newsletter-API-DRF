from rest_framework.test import APITestCase
from newsletter_app.models import Newsletters
from tags_app.models import Tag
from users_app.models import User

class TestNewsLetter(APITestCase):
    
    def setUp(self):
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
            imagen = 'newsletter.png',
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
        
    def test_post_newsletter(self):
        data = {
            'nombre' : 'newsletter 2',
            'description' : 'description 2',
            'imagen' : 'newsletter-2.png',
            'target': 2,
            'frecuencia' : 'frecuencia 2',
            'tags' : [self.tag.id],
            'fecha_creacion' : '2020-04-06'
        }
        response = self.client.post(f'{self.host}/newsletter/', data)
        self.assertEqual(response.status_code, 400, response.data)
        self.assertEqual(Newsletters.objects.all().count(), 1)
        