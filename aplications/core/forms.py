from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ClienteProfile

# Formulario para registro de clientes con todos los datos
class RegistroClienteForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nombre_empresa = forms.CharField(max_length=150)
    rut = forms.CharField(max_length=12)
    telefono = forms.CharField(max_length=20, required=False)
    direccion = forms.CharField(max_length=255, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 
                  'nombre_empresa', 'rut', 'telefono', 'direccion']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            if not hasattr(user, 'clienteprofile'):
                ClienteProfile.objects.create(
                    user=user,
                    nombre_empresa=self.cleaned_data['nombre_empresa'],
                    rut=self.cleaned_data['rut'],
                    telefono=self.cleaned_data.get('telefono'),
                    direccion=self.cleaned_data.get('direccion')
                )
        return user

# Formulario básico de registro solo usuario
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control-plaintext', 'readonly': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control-plaintext', 'readonly': True}),
        }

class ClienteProfileForm(forms.ModelForm):
    class Meta:
        model = ClienteProfile
        fields = ['nombre_empresa', 'rut', 'telefono', 'direccion']
        widgets = {
            'nombre_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }