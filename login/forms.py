from django import forms

class FormularioLogin(forms.Form):

    usuario = forms.CharField(label="Nombre de usuario", max_length=100)
    contrasenia = forms.CharField(label="Introduzca contraseña", widget=forms.PasswordInput)

class FormularioRegister(forms.Form):

    usuario = forms.CharField(label="Nombre del usuario", max_length=100)
    email = forms.EmailField(label="Ingresa email")
    contrasenia = forms.CharField(label="Ingresa contraseña", widget=forms.PasswordInput)