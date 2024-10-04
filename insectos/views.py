from django.shortcuts import render
from .models import Insectos

# Create your views here.

def insectos(request):

    insectos = Insectos.objects.all()
    return render(request, "insectos/insectos.html", {"insectos":insectos})
