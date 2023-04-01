from django.urls import path

from AppCoder.views import *

urlpatterns = [
    path('cursos', cursos, name="AppCoderCursos"),
    path('cursos/crear', crear_curso, name="AppCoderCrearCurso"),
    path('cursos/eliminar/<camada>', elimiar_curso, name="AppCoderEliminarCurso"),
    path('cursos/editar/<camada>', editar_curso, name="AppCoderEditarCurso"),
    path('buscar_curso', busqueda_curso, name="AppCoderBuscarCurso"),
    path('curso/<nombre>/<camada>', crear_curso1, name="AppCoderCurso"),
    path('estudiantes', estudiantes, name="AppCoderEstudiantes"),
    path('profesores', profesores, name="AppCoderProfesores"),
]
