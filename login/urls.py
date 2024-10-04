from django.urls import path
from login.views import *

urlpatterns = [
    path('', login, name="login"),
    path('register/', register, name="register"),
]