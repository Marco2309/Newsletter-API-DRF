from django.db import models


class Tag(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField()
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
