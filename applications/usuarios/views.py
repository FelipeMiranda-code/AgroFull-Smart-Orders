from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Formularios y modelos propios
from .forms import RegistroForm, DireccionForm
from .models import Direccion


# ===========================
#   REGISTRO
# ===========================
def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)     # Loguear automáticamente
            messages.success(request, "Registro exitoso!")
            return redirect("inicio")
    else:
        form = RegistroForm()

    return render(request, "usuarios/registro.html", {"form": form})


# ===========================
#   LOGIN
# ===========================
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("inicio")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    else:
        form = AuthenticationForm()

    return render(request, "usuarios/login.html", {"form": form})


# ===========================
#   LOGOUT
# ===========================
def logout_view(request):
    logout(request)
    return redirect("login")


# ===========================
#   DIRECCIONES - LISTAR
# ===========================
@login_required
def lista_direcciones(request):
    direcciones = request.user.direcciones.all()
    return render(request, "usuarios/lista_direcciones.html", {"direcciones": direcciones})


# ===========================
#   DIRECCIONES - CREAR
# ===========================
@login_required
def crear_direccion(request):
    if request.method == "POST":
        form = DireccionForm(request.POST)
        if form.is_valid():
            direccion = form.save(commit=False)
            direccion.usuario = request.user

            # Si marca como principal, desmarcar otras
            if direccion.principal:
                request.user.direcciones.update(principal=False)

            direccion.save()
            messages.success(request, "Dirección guardada.")
            return redirect("lista_direcciones")
    else:
        form = DireccionForm()

    return render(request, "usuarios/form_direccion.html", {"form": form})


# ===========================
#   DIRECCIONES - EDITAR
# ===========================
@login_required
def editar_direccion(request, pk):
    direccion = get_object_or_404(Direccion, pk=pk, usuario=request.user)

    if request.method == "POST":
        form = DireccionForm(request.POST, instance=direccion)

        if form.is_valid():
            direccion = form.save(commit=False)

            # Si esta dirección queda como principal
            if direccion.principal:
                request.user.direcciones.update(principal=False)

            direccion.save()
            messages.success(request, "Dirección actualizada.")
            return redirect("lista_direcciones")

    else:
        form = DireccionForm(instance=direccion)

    return render(request, "usuarios/form_direccion.html", {"form": form})


# ===========================
#   DIRECCIONES - BORRAR
# ===========================
@login_required
def borrar_direccion(request, pk):
    direccion = get_object_or_404(Direccion, pk=pk, usuario=request.user)

    if request.method == "POST":
        direccion.delete()
        messages.success(request, "Dirección eliminada.")
        return redirect("lista_direcciones")

    return render(request, "usuarios/confirmar_borrar.html", {"direccion": direccion})


from django.contrib.auth.decorators import login_required

@login_required
def perfil(request):
    return render(request, "usuarios/perfil.html")
