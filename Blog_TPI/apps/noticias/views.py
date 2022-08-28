from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin #esto es para vista basada en clase
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from datetime import datetime

def llenar_dias():
    lista = []
    for i in range(1,31):
        lista.append(i)
    return lista 

def llenar_anios():
    lista = []
    for i in range(2022,2300):
        lista.append(i)
    return lista

meses = [1,2,3,4,5,6,7,8,9,10,11,12]
dias = llenar_dias()
anios = llenar_anios()

# Create your views here.
def Listar(request):

 #Creo un diccionario para pasar datos al template
    ctx = {} 
    #Buscar las noticias de la BD
    autor = request.POST.get('filtrar_autor',None)
    titulos = request.POST.get('filtrar_titulos',None)
    dia = request.POST.get('dia',None)
    mes = request.POST.get('mes',None)
    anio = request.POST.get('anio',None)
    
    if dia and mes and anio:
        fecha = datetime(int(anio),int(mes),int(dia))
        todas = Noticia.objects.filter(creado = fecha)
    elif titulos:
        todas=Noticia.objects.filter(titulo = titulos)
    elif autor:
        todas=Noticia.objects.filter(autor = autor)
    else:
        todas = Noticia.objects.all()

    #Pasarlo al template
    ctx['notis'] = todas    
    ctx['meses'] = meses
    ctx['dias'] = dias 
    ctx['anios'] = anios 
    return render(request,'noticias/listar_noticias.html',ctx)
    
@login_required
def Mostrar(request,pk):
    ctx = {}
    publicacion = Noticia.objects.get(pk = pk)
    ctx['publi'] = publicacion
    return render(request,'noticias/noticia.html',ctx)


def Agregar_Comentario(request,pk):
    texto_c = request.POST.get('coment')
    noti = Noticia.objects.get(pk = pk)
    c = Comentario.objects.create(noticia = noti, texto = texto_c, usuario = request.user)

    return HttpResponseRedirect(reverse_lazy('noticias:mostrar', kwargs={'pk':pk}))

"""
class Mostrar(LoginRequiredMixin, Detailvies):
    model = Noticia
    template_name = 'noticias/mostrar.html'
"""