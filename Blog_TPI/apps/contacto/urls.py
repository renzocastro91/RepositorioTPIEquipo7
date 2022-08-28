from django.urls import path
from . import views 

# LA URL EMPIEZA DESDE NOTICIAS/ y todas las urls que se listen acá
app_name = 'contacto'
urlpatterns = [
    path('principal/', views.Principal, name = 'principal'),
]