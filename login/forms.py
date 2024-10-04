from django import forms

class FormularioLogin(forms.Form):

    usuario = forms.CharField(label="Nombre de usuario", max_length=100)
    contrasenia = forms.CharField(label="Introduzca contraseña", widget=forms.PasswordInput)
