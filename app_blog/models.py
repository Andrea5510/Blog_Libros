from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PostsLibros(models.Model):

    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100, null=True)
    cuerpo = models.TextField(max_length=1000, null=True) 
    creador=  models.CharField(max_length=100, null=True)
    fecha_publicacion = models.DateField()
    portada= models.ImageField(upload_to = 'post_images', null = True, blank = True)

class Mensajes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    mensaje = models.CharField(max_length=400)
    def __str__(self):
        return f"id: {self.id}, user: {self.user}, mensaje: {self.mensaje}"