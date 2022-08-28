from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre_integrante = models.CharField(max_length=80,null=True, blank=True)
    recurso_foto= models.ImageField(upload_to='contacto',null=True, blank=True)
    url_insta = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nombre_integrante

