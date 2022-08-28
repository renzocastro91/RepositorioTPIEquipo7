# Create your views here.
from django.shortcuts import render
from .models import *

# Create your views here.
def Principal(request):
    ctx={}
    todas = Contacto.objects.all()
    ctx['contactos'] = todas
    return render(request,'contacto/principal.html',ctx)