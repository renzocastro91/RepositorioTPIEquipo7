from django.shortcuts import render

# Create your views here.
def Principal(request):
    return render(request,'login/principal.html')

def Registro(request):
    return render(request,'login/registro.html')