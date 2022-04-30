
from django.urls import path
from app_blog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('pages/', LibrosList.as_view(), name = "Lista"),
    path('pages/<pk>/', LibrosDetail.as_view(), name = "Detalle"),
    path('editar/<pk>/', LibrosUpdate.as_view(), name = "Editar"),
    path('borrar/<pk>/', LibrosDelete.as_view(), name = "Eliminar"),
    path('nuevo/', LibrosCreate.as_view(), name = "Crear"),
    path('postsBuscar/', buscar_post, name = "Buscar_Posts"),
    path('messages/', mensajes, name="Mensajes")
    ]