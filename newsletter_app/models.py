from django.db import models


class Newsletters(models.Model):
    nombre = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to='imagenes', null=True)
    target = models.IntegerField
    frecuencia = models.CharField(max_length=50)
    fecha_creacion = models.DateField()
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
