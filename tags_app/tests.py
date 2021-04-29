from rest_framework.test import APITestCase
from tags_app.models import Tag

class TestTags(APITestCase):
    
    def setUp(self):
        self.host = 'http://127.0.0.1:8000'
        self.tag = Tag.objects.create(
            nombre = 'tag 1',
            slug = 'slug 1',
            fecha_creacion = '2021-04-27'
        )    
    
    def tes_get_tags(self):
        response = self.client.get(f'{self.host}/tags/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Tag.objects.all().count(), 1)
    
    def test_post_tags(self):
        data={
            "nombre" : 'tag 2',
            "slug" : 'slug 2',
            "fecha_creacion" : '2021-04-27'
        }
        response = self.client.post(f'{self.host}/tags/', data)
        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(Tag.objects.get(id=2).nombre, 'tag 2')
        
    def test_put_tags(self):
        data={
            "nombre" : 'tag actualizado',
            "slug" : 'slug actualizado',
            "fecha_creacion" : '2021-04-26'
        }
        nombreTag = Tag.objects.get(id = self.tag.id).nombre
        response = self.client.put(f'{self.host}/tags/{self.tag.id}/',data)
        self.assertEqual(response.status_code, 200, response.data)
        self.assertNotEqual(nombreTag, data['nombre'])
        
    def test_delete_tags(self):
        response = self.client.delete(f'{self.host}/tags/{self.tag.id}/')
        self.assertEqual(len(Tag.objects.all()), 0)
        