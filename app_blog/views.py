from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from django.urls import reverse_lazy

from app_blog.models import PostsLibros, Mensajes
from .forms import PostForm, MensajesForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

# Create your views here.

def buscar_post(request):

    data = request.GET.get('post', "")
    mensaje = ""
    error = ""

    if data:
        posts = PostsLibros.objects.filter(titulo__icontains= data)
        print(posts)
        if posts:
            return render(request, 'app_blog/buscar_post.html', {"posts": posts, "nombre": data})
        else: 
            error = "No existe Libro"
    else: 
        mensaje = "Ingrese un libro" 

    return render(request, 'app_blog/buscar_post.html', {"error": error, "mensaje": mensaje}) 

#Libros
class LibrosList(ListView):

    model = PostsLibros
    template_name = "app_blog/libros_lista.html"

class LibrosDetail(DetailView):

    model = PostsLibros
    template_name = "app_blog/libros_detalle.html"

class LibrosCreate(CreateView):

    model = PostsLibros
    success_url = "/pages"
    fields = ['titulo','subtitulo','cuerpo','creador','fecha_publicacion','portada']

class LibrosUpdate(UpdateView):

    model = PostsLibros
    success_url = "/pages"
    fields = ['titulo','subtitulo','cuerpo','creador','fecha_publicacion','portada']

class LibrosDelete(DeleteView):

    model = PostsLibros
    success_url = "/pages"

@login_required
def mensajes (request):

    mensajeForm = MensajesForm()
    mensaje = Mensajes.objects.all()
    if request.method == 'POST':
        contenido_mensaje = MensajesForm(request.POST)
        if contenido_mensaje.is_valid():
            data = contenido_mensaje.cleaned_data
            mensaje = Mensajes(mensaje=data["mensaje"], user=request.user)
            mensaje.save()
            return redirect('Mensajes')
        else:
            return render(request, 'app_blog/mensajes.html', {"mensajeForm": contenido_mensaje,"mensaje": mensaje})
    else:
        return render(request, 'app_blog/mensajes.html', {"mensajeForm": mensajeForm,  "mensaje": mensaje})

