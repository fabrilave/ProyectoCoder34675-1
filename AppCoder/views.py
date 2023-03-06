from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso


def cursos(request):
    return render(request, "index.html")


def estudiantes(request):
    return render(request, "index.html")


def profesores(request):
    return render(request, "index.html")
