from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Direccion

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ["nombre", "calle", "numero", "comuna", "ciudad", "referencia", "principal"]
