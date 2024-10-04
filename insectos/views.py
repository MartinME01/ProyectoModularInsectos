from django.shortcuts import render

# Create your views here.

def insectos(request):

    return render(request, "insectos/insectos.html", {"insectos":insectos})
