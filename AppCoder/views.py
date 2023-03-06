from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso


# Create your views here.
def guardar_curso(request, camada):
    curso = Curso(nombre="Python", camada=camada)
    curso.save()
    return HttpResponse("usuario creado exitosamente")
