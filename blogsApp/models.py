from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length=40)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='templates/blogs-imagenes')
    fechaBlog = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Titulo{self.titulo}, Contenido{self.contenido}, FechaBlog{self.fechaBlog}, Autor{self.autor}"

class Usuarios(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre {self.nombre}, Apellido{self.apellido}, Email{self.email}"
