from django.shortcuts import render, redirect
from blogsApp.models import *
from blogsApp.forms import *
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "base/base.html")
def registroCursos(request):
    if request.method == 'POST':
        registroCursos = CursoForm(request.POST)

        if registroCursos.is_valid():
            info = registroCursos.cleaned_data
            registroCurso = Curso(
                nombre=info['nombre'],
                camada=info['camada']
            )
            registroCurso.save()

    all_cursos = Curso.objects.all()
    context = {
        "cursos": all_cursos,
        "formRegistroCursos": CursoForm()
    }
    return render(request, "AppCoder/registroCursos.html", context=context)

def busquedaCursos(request):
    form_busquedaCurso = BusquedaCursoForm(request.GET)
    if form_busquedaCurso.is_valid():
        info = form_busquedaCurso.cleaned_data
        cursosFiltrados = Curso.objects.filter(nombre__icontains=info['nombre'])
    else:
        cursosFiltrados = None

    context = {
        "form_busqueda": BusquedaCursoForm(),
        'cursos': cursosFiltrados
    }

    return render(request, "AppCoder/busquedaCursos.html", context=context)

def registroProfesores(request):

    if request.method == 'POST':
        formRegistroProfesores = ProfesorForm(request.POST)

        if formRegistroProfesores.is_valid():
            info = formRegistroProfesores.cleaned_data
            registroProfesor = Profesor(
                nombre=info['nombre'],
                apellido=info['apellido'],
                email=info['email'],
                profesion=info['profesion']
            )
            registroProfesor.save()
            messages.success(request, '¡Profesor registrado con éxito!')

    context = {
        "formRegistroProfesores": ProfesorForm()
    }

    return render(request, "AppCoder/registroProfesores.html", context=context)

def registroEstudiante(request):

    if request.method == "POST":
        estudiante = Estudiante(nombre=request.POST['nombre'],
                                apellido=request.POST['apellido'],
                                email=request.POST['email'])
        estudiante.save()

        return redirect('Home')

    return render(request, "AppCoder/registroEstudiante.html")

def eliminarCurso(request):
    pass
