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
            fecha_creacion = '2021-04-27T17:21:01.757261Z'
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
        # self.newsletter.user.add(self.user1)
        
    def test_get_newsletter(self):
        response = self.client.get(f'{self.host}/newsletter/')
        self.assertEqual(response.status_code, 200)
        