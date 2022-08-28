from django.urls import path
from . import views 
from django.contrib.auth import views as auth
# LA URL EMPIEZA DESDE NOTICIAS/ y todas las urls que se listen acá
app_name = 'login'
urlpatterns = [
    path('principal/', views.Principal, name = 'principal'),
    path('registro/',views.Registro, name='registro')
]