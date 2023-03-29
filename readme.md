def crear_curso(request):
    if request.method == 'POST':
        mi_formulario = CursoForms(request.POST)

        if mi_formulario.is_valid():
            informacion= mi_formulario.cleaned_data
            curso_save = Curso(
                nombre=informacion['nombre'],
                camada = informacion['camada']
                )
            curso_save.save()
    mi_formulario = CursoForms(
        context = {'form' : mi_formulario}
    )
    return render(request, "AppCoder/crear_curso.html", context=context)