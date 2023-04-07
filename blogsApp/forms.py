from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blogsApp.models import Blog, Comentario
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen']

class UsuariosForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=40)
    nombre = forms.CharField(min_length=3, max_length=40)
    apellido = forms.CharField(min_length=3, max_length=40)
    email = forms.EmailField()
    password1 = forms.CharField(min_length=8, label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=8, label='Repetir contraseña', widget=forms.PasswordInput)

class BusquedaBlogForm(forms.Form):
    titulo = forms.CharField(max_length=40)

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
