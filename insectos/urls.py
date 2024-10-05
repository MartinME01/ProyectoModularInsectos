from django.urls import path
from insectos.views import *

urlpatterns = [
    path('', insectos, name="insectos"),
]