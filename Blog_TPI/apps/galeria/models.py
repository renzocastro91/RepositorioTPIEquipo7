from django.db import models

# Create your models here.

class Imagen(models.Model):
    titulo = models.CharField(max_length=70)
    recurso_imagen= models.ImageField(upload_to='galeria',null=True, blank=True)

    def __str__(self):
        return self.titulo

