# Create your views here.
# Create your views here.
from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def Principal(request):
    ctx = {}

    todas = Evento.objects.all()

    ctx['eventos'] = todas

    return render(request,'eventos/principal.html',ctx)

@login_required
def Mostrar(request,pk):
    ctx = {}
    evento = Evento.objects.get(pk = pk)
    ctx['evento'] = evento
    return render(request,'eventos/detalle_evento.html',ctx)