from turtle import ondrag
from django.db import models
from datetime import datetime, date
# Create your models here.

class Modalidad(models.Model):
    modalidad = models.CharField(max_length=70)

    def __str__(self):
        return self.modalidad

class Estado(models.Model):
    estado = models.CharField(max_length=70)

    def __str__(self):
        return self.estado

class Evento(models.Model):
    titulo= models.CharField(max_length=70)
    imagen= models.ImageField(upload_to='Evento',null=True, blank=True)
    modalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE, null=False)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE,null=False)
    fecha_evento = models.DateField(auto_now_add=False,auto_now=False, blank=True)
    fecha_carga = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    #fecha=models.DateField(auto_now_add=False, auto_now=False, blank=True)
    description= models.TextField()
    
    class Meta:
        ordering= ('fecha_evento',)

    def __str__(self):
        return self.titulo