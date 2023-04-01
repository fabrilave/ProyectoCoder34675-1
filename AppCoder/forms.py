from django import forms

from AppCoder.models import Curso, Estudiantes, Profesor


class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = "__all__"


class EstudianteForm(forms.ModelForm):

    class Meta:
        model = Estudiantes
        fields = "__all__"


class ProfesorForm(forms.ModelForm):

    class Meta:
        model = Profesor
        fields = "__all__"


class BusquedaCursoForm(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=40)
