from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse

from app_login.forms import RegistroUsuarios, EditarUsuarios, AvatarFormulario
from app_login.models import Avatar

from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def inicio(request):

    if request.user.is_authenticated:

        avatar = Avatar.objects.filter(user=request.user)

        if len(avatar) > 0:
            imagen = avatar[0].imagen.url

            return render(request, 'app_login/base.html', {"imagen_url":imagen})  

        else:
            imagen = '/media/avatars/NPCMI7NVIRGLBJXCI3VYOEWGPE.jpg'
            return render(request, 'app_login/base.html',{"imagen_url":imagen})

    else:

        return render(request, 'app_login/base.html')


def about_me(request):
    return render(request, 'app_login/about.html')

def iniciar_sesion(request):

    if request.method == "POST":
            form = AuthenticationForm()
            formulario = AuthenticationForm(request, data=request.POST)

            if formulario.is_valid():
                data = formulario.cleaned_data

                nombre_usuario = data.get("username")
                contrasenia = data.get("password")

                usuario = authenticate(username=nombre_usuario, password=contrasenia)

                if usuario is not None:
                    login(request, usuario)
                    return redirect("Inicio")
                    
            else:
                
                return render(request, "app_login/login.html", {"error": "Formulario erroneo","form": form})    
    else:
            form = AuthenticationForm()
            return render(request, "app_login/login.html", {"form": form})


def registro(request):

    if request.method == "POST":

        form = RegistroUsuarios(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()

            return render(request, "app_login/base.html", {"mensaje":"El usuario ha sido creado exitosamente"})
        
    else:

        form = RegistroUsuarios()

    return render(request, "app_login/signup.html", {"form":form})


@login_required
def editar_usuario(request):
    usuario = request.user
        
    if request.method == "POST":
                        
        miFormulario = EditarUsuarios(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.set_password(informacion["password1"])
            usuario.save()

            return render(request, 'app_login/editarperfil.html', {"edit_success": True})

        else:
        
            return render(request, 'app_login/base.html', {"miFormulario": miFormulario})
    else: 

        miFormulario = EditarUsuarios(initial={'email': usuario.email})

    return render(request, "app_login/editarperfil.html", {"miFormulario":miFormulario, "usuario": usuario})
      

@login_required
def cargar_avatar(request):
    usuario = request.user
    
    if usuario.groups.filter(name='admin').exists():

        if request.method=="POST":

            formulario = AvatarFormulario(request.POST, request.FILES)

            if formulario.is_valid():

                usuario = request.user
                avatar = Avatar.objects.filter(user = usuario)

                if len(avatar)>0:
                    avatar = avatar[0]
                    avatar.imagen = formulario.cleaned_data["imagen"]
                    avatar.save()

                else:
                    avatar = Avatar(user = usuario, imagen = formulario.cleaned_data["imagen"])
                    avatar.save()
                
                return redirect("Inicio")
        else:
            formulario = AvatarFormulario()
            return render(request, "app_login/cargar_imagen.html", {"form":formulario})
    else: 
        
        return render(request, "app_login/cargar_imagen.html", {"error": "El usuario no tiene permisos para realiza esta acción"})  


