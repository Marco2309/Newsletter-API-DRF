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
            fecha_creacion = '2021-03-01',
            created_at = '2021-03-01',
            update_at = '2021-01-02'
        )
        self.user = User.objects.create(
            username='juancorrea',
            password = 'jusecovi11',
            is_administrador = True
        )
        self.newsletter = Newsletters.objects.create(
            nombre = 'newsletter 1',
            description = 'description 1 ',
            imagen = 'newsletter.png',
            target = 1,
            frecuencia = 'frecuencia 1',
            fecha_creacion = '2020-04-06'
        )
        self.newsletter.tags.add(self.tags)
        self.newsletter.user.add(self.user)
        
    def test_get_newsletter(self):
        response = self.client.get(f'{self.host}/newsletter/')
        self.assertEqual(response.status_code, 200)
        
'''Agregar el tema del target al modelo de la base de datos 
verificar que exista en la db para realizar la prueba 
'''