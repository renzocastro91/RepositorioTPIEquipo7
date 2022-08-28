from django.urls import path
from . import views

# LA URL EMPIEZA DESDE NOTICIAS/ y todas las urls que se listen acá
app_name = 'noticias'
urlpatterns = [
    path('listar/', views.Listar, name = 'listar_noticias'),
    path('mostrar/<int:pk>',views.Mostrar, name='mostrar'),
    path('add_comentario/<int:pk>',views.Agregar_Comentario, name='agregar_comentario'),
]