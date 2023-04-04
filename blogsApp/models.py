from django.db import models

# Create your models here.

class Users(models.Model):
    nickUser = models.CharField(max_length=15)
    nombreUser = models.CharField(max_length=40)
    apellidoUser = models.CharField(max_length=40)
    edadUser = models.IntegerField()
    emailUser = models.EmailField()
    def __str__(self):
        return f"NickUser{self.nickUser}, edadUser{self.edadUser}, EmailUser{self.emailUser}"

class Blogs(models.Model):
    tittleBlogs = models.CharField(max_length=42)
    fechaBlogs = models.DateField()
    textBlogs = models.TextField()
    imgBlogs = models.ImageField(upload_to='publicacion_imagenes')
    autorBlogs = models.ForeignKey(Users, on_delete=models.CASCADE)
    def __str__(self):
        return f"TittleBlogs{self.tittleBlogs}, FechaBlogs{self.fechaBlogs}, TextBlogs{self.textBlogs}, ImgBlogs{self.imgBlogs}, AutorBlogs{self.autorBlogs}"

class comentarioBlog(models.Model):
    fechaComentarioBlog = models.DateField()
    textComentarioBlog = models.TextField()

    def __str__(self):
        return f"FechaComentarioBlog{self.fechaComentarioBlog}, TextComentarioBlog{self.textComentarioBlog}"
