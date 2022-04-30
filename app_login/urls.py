from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import inicio, about_me, iniciar_sesion, registro, editar_usuario, cargar_avatar

urlpatterns = [
    path('', inicio, name = "Inicio"),
    path('about/', about_me, name = "Acerca de mi"),
    path('accounts/login', iniciar_sesion, name = "Login"),
    path('accounts/logout', LogoutView.as_view(template_name = 'app_login/logout.html'), name = "Logout"),
    path('accounts/signup', registro, name = "Signup"),
    path('accounts/profile', editar_usuario, name = "Edit"),
    path('', include("app_blog.urls")),
    path('cargar_imagen', cargar_avatar, name="CargarImagen")
    ]