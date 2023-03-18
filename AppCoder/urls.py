from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('cursos', cursos, name="AppCoderCursos"),
    path('buscar_curso', busqueda_curso, name='AppCoderBuscarCurso'),
    path('curso/<nombre>/<camada>', crear_curso, name="AppCoderCurso"),
    path('estudiantes', estudiantes, name='AppCoderEstudiantes'),
    path('profesores', profesores, name='AppCoderProfesores'),

]
