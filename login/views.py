from django.shortcuts import render
from .forms import FormularioLogin

# Create your views here.

def login(request):

    if request.method == "POST":

        formularioLogin = FormularioLogin(request.POST)

        if formularioLogin.is_valid:

            #informacionLogin = formularioLogin.cleaned_data

            return render(request, "login/gracias.html")

    else:

        formularioLogin = FormularioLogin()


    return render(request, "login/login.html", {"form":formularioLogin})
