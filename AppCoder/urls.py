from django.urls import path

from AppCoder.views import *

urlpatterns = [
    path('cursos', cursos),
    path('estudiantes', estudiantes),
    path('profesores', profesores),
]
