from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from blogsApp.models import *
from blogsApp.forms import BlogForm, UsuariosForm, BusquedaBlogForm, ComentarioForm
from django.contrib import messages
from django.db import IntegrityError, transaction


# Create your views here.
def home(request):
    return render(request, "base/base.html")

def about(request):
    return render(request, "base/about.html")
def crear_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.autor = request.user
            blog.save()
    else:
        form = BlogForm()
    return render(request, "blog/registroBlogs.html", {'form': form})

def buscar_blogs(request):
    form = BusquedaBlogForm(request.GET)
    if form.is_valid():
        info = form.cleaned_data
        blogsFiltrados = Blog.objects.filter(titulo__icontains=info['titulo'])
    else:
        blogsFiltrados = None
    context = {
        "form_busqueda": BusquedaBlogForm(),
        'blogs': blogsFiltrados
    }
    return render(request, "blog/busquedaBlogs.html", context=context)

def listar_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/listarBlogs.html', {'blogs': blogs})


def detalle_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    comentarios = Comentario.objects.filter(blog=blog)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.blog = blog
            comentario.save()
            return redirect('blogsAppDetalleBlog', pk=pk)
    else:
        form = ComentarioForm()

    context = {
        'blog': blog,
        'comentarios': comentarios,
        'form': form
    }
    return render(request, 'blog/detalleBlog.html', context=context)

@transaction.atomic
def registro_usuario(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 != password2:
                messages.error(request, 'Las contraseñas no coinciden')
                return redirect('blogsAppRegistroUsuarios')
            try:
                with transaction.atomic():
                    user = User(username=username, password=make_password(password1))
                    user.save()
            except IntegrityError:
                messages.error(request, 'El nombre de usuario ya está registrado')
                return redirect('blogsAppRegistroUsuarios')
            messages.success(request, '¡Usuario registrado con éxito!')
            return redirect('blogsAppRegistroUsuarios')
    else:
        form = UsuariosForm()
    return render(request, 'blog/registroUsuarios.html', {'form':form})

def login_usuario(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info = form.cleaned_data
            user = authenticate(username=info['username'], password=info['password'])
            if user:
                login(request, user)
                return redirect('Home')
        # Si las credenciales no son válidas, se muestra un mensaje de error
        messages.error(request, 'Usuario o contraseña incorrecto, por favor intente de nuevo.')
    else:
        form = AuthenticationForm()
    context = {
        "form": form
    }
    return render(request, 'blog/loginUsuario.html', context=context)

def eliminarBlog(request, pk):
    get_blog = Blog.objects.get(pk=pk)
    get_blog.delete()
    return redirect('Home')

def editar_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.autor = request.user
            blog.save()
            blogs = Blog.objects.all()
            return render(request, 'blog/listarBlogs.html', {'blogs': blogs})
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/editarBlogs.html', {'form': form, 'blog': blog})

