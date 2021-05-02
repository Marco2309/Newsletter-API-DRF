from django.db import models
from tags_app.models import Tag
from users_app.models import CustomUser

class Newsletters(models.Model):
    nombre = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to='imagenes', null=True)
    target = models.IntegerField()
    frecuencia = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag, related_name='newsletters')
    user = models.ForeignKey(
        CustomUser, related_name='newsletters', on_delete=models.SET_NULL, null=True)
    users = models.ManyToManyField(CustomUser, related_name='subscriptions')
    members = models.ManyToManyField(CustomUser, related_name='editable')
    voters = models.ManyToManyField(CustomUser, related_name='voted')
    fecha_creacion = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
