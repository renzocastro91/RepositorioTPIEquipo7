from django.shortcuts import render
from .models import *


# Create your views here.
def Principal(request):
    ctx={}
    todas = Imagen.objects.all()
    ctx['imagenes'] = todas

    return render(request,'galeria/principal.html',ctx)