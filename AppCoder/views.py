from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from AppCoder.models import Curso
from AppCoder.forms import CursoForm, BusquedaCursoForm


def busqueda_curso(request):
    #mostrar datos filtrados
    mi_formulario = BusquedaCursoForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        cursos_filtrados = Curso.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "cursos": cursos_filtrados
        }

        return render(request, "AppCoder/busqueda_curso.html", context=context)


def editar_curso(request, camada):
    get_curso = Curso.objects.get(camada=camada)

    if request.method == "POST":
        mi_formulario = CursoForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            get_curso.nombre = informacion['nombre']
            get_curso.camada = informacion['camada']

            get_curso.save()
            return redirect("AppCoderCursos")


    context = {
        "camada": camada,
        "form": CursoForm(initial={
            "nombre": get_curso.nombre,
            "camada": get_curso.camada
        })
    }
    return render(request, "AppCoder/editar_curso.html", context=context)


def crear_curso(request):
    if request.method == "POST":
        mi_formulario = CursoForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso_save = Curso(
                nombre=informacion['nombre'],
                camada=informacion['camada']
            )
            curso_save.save()
            return redirect("AppCoderCursos")

    context = {
        "form": CursoForm()
    }
    return render(request, "AppCoder/crear_curso.html", context=context)


def elimiar_curso(request, camada):
    get_curso = Curso.objects.get(camada=camada)
    get_curso.delete()

    return redirect("AppCoderCursos")

def cursos(request):

    all_cursos = Curso.objects.all()
    context = {
        "cursos": all_cursos,
        "form_busqueda": BusquedaCursoForm(),
    }
    return render(request, "AppCoder/cursos.html", context=context)


def crear_curso1(request, nombre, camada):
    save_curso = Curso(nombre=nombre, camada=int(camada))
    save_curso.save()
    context = {
        "nombre": nombre
    }
    return render(request, "AppCoder/save_curso.html", context)


def estudiantes(request):
    return render(request, "base.html")


def profesores(request):
    return render(request, "base.html")
