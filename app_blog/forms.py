from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    subtitulo = forms.CharField(max_length=100)
    cuerpo = forms.CharField(max_length=4000, widget=forms.Textarea(attrs={"rows": 12}))
    creador=  forms.CharField(max_length=100)
    fecha_publicacion = forms.DateField()
    portada= forms.ImageField()
    
class MensajesForm(forms.Form):
    mensaje = forms.CharField(max_length=400)