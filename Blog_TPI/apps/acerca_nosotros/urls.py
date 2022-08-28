from django.urls import path
from . import views 

# LA URL EMPIEZA DESDE NOTICIAS/ y todas las urls que se listen acá
app_name = 'acerca_nosotros'
urlpatterns = [
    path('principal/', views.Principal, name = 'acerca_nosotros'),
    path('conocenos_mas/',views.Segundaparte, name= 'conocenos_mas'),
    path('conocenos_mas2/',views.Terceraparte, name= 'conocemos_mas2'),
]