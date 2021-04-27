from django.db import models


class Tag(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
