from django.shortcuts import render
from .models import *

# Create your views here.
def Principal(request):
    ctx = {}
    todas = Pregunta.objects.all()
    ctx['preguntas'] = todas

    return render(request,'fechas_importantes/principal.html',ctx)

