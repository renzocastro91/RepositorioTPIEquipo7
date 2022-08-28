from django.shortcuts import render

# Create your views here.
def Principal(request):
    return render(request,'acerca_nosotros/acerca_nosotros.html')

def Segundaparte(request):
    return render(request,'acerca_nosotros/2.html')

def Terceraparte(request):
    return render(request,'acerca_nosotros/3.html')