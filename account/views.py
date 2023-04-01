from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from account.models import Avatar
from account.forms import UserRegisterForm


def editar_usuario(request):

    user = request.user

    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():

            informacion = form.cleaned_data

            user.username = informacion["username"]
            user.email = informacion["email"]
            user.is_staff = informacion["is_staff"]

            try:
                user.avatar.imagen = informacion["imagen"]
            except:
                avatar = Avatar(user=user, imagen=informacion["imagen"])
                avatar.save()
            
            

            user.save()
            return redirect("accountLogin")

    form = UserRegisterForm(initial={
        "username": user.username,
        "email":user.email,
        "is_staff":user.is_staff
    })

    context = {
        "form": form,
        "titulo": "Editar usuario",
        "enviar": "Editar"
    }

    return render(request, "form.html", context=context)

def register_account(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("accountLogin")

    # form = UserCreationForm()
    form = UserRegisterForm()
    context = {
        "form": form,
        "titulo": "Registrar usuario",
        "enviar": "registrar"
    }
    return render(request, "form.html", context=context)


def login_account(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            informacion = form.cleaned_data

            user = authenticate(username=informacion['username'], password=informacion['password'])
            if user:
                login(request, user)

                return redirect("AppCoderCursos")
            else:
                return redirect("AppCoderEstudiantes")

    form = AuthenticationForm()
    context = {
        "form": form,
        "titulo": "Login",
        "enviar": "iniciar"
    }
    return render(request, "form.html", context=context)
