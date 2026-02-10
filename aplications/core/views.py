from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth import logout
from .forms import RegistroClienteForm, RegistroForm, UserForm
from .models import Producto, Categoria


# ---- REGISTRO ----
class RegistroView(CreateView):
    template_name = "core/registro.html"
    form_class = RegistroForm
    success_url = reverse_lazy("login")

class RegistroClienteView(CreateView):
    template_name = "core/registro_cliente.html"
    form_class = RegistroClienteForm
    success_url = reverse_lazy("login")


# ---- LOGIN ----
class CustomLoginView(LoginView):
    template_name = "core/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


# ---- LOGOUT SOLO POST ----
@require_POST
def cerrar_sesion(request):
    logout(request)
    messages.success(request, "👋 Has cerrado sesión correctamente.")
    return redirect("login")


# ---- VISTAS PRINCIPALES ----
class HomeView(TemplateView):
    template_name = "core/index.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "core/dashboard.html"
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos_count'] = 42
        context['pedidos_count'] = 15
        context['inventario_count'] = 378
        context['clientes_count'] = 90
        return context


# ---- PRODUCTOS ----
def lista_productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, "productos/lista.html", {"productos": productos, "categorias": categorias})


def productos_por_categoria(request, categoria_id):
    productos = Producto.objects.filter(categoria_id=categoria_id)
    categorias = Categoria.objects.all()
    categoria = Categoria.objects.get(id=categoria_id)
    return render(request, "productos/lista.html", {
        "productos": productos,
        "categorias": categorias,
        "categoria_actual": categoria
    })


# ---- CARRITO ----
def agregar_al_carrito(request, producto_id):
    carrito = request.session.get("carrito", {})
    carrito[str(producto_id)] = carrito.get(str(producto_id), 0) + 1
    request.session["carrito"] = carrito
    messages.success(request, "🛒 Producto agregado al carrito.")
    return redirect("productos")


def ver_carrito(request):
    carrito = request.session.get("carrito", {})
    productos = Producto.objects.filter(id__in=carrito.keys())
    total = 0
    detalle = []
    for producto in productos:
        cantidad = carrito[str(producto.id)]
        subtotal = cantidad * producto.precio
        total += subtotal
        detalle.append({"producto": producto, "cantidad": cantidad, "subtotal": subtotal})
    return render(request, "carrito/ver.html", {"detalle": detalle, "total": total})


def eliminar_item(request, producto_id):
    carrito = request.session.get("carrito", {})
    carrito.pop(str(producto_id), None)
    request.session["carrito"] = carrito
    messages.info(request, "🗑 Producto eliminado del carrito.")
    return redirect("carrito")


def checkout(request):
    carrito = request.session.get("carrito", {})
    if not carrito:
        messages.error(request, "⚠️ Tu carrito está vacío.")
        return redirect("carrito")
    request.session["carrito"] = {}
    messages.success(request, "✔ Compra realizada correctamente.")
    return redirect("productos")


# ---- PERFIL USUARIO ----
@login_required
def dashboard(request):
    return render(request, "usuarios/dashboard.html")


def detalle_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, "productos/detalle.html", {"producto": producto})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ClienteProfileForm
from .models import ClienteProfile

@login_required
def mi_cuenta(request):
    user = request.user
    # Obtener o crear perfil si no existe
    perfil, created = ClienteProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        perfil_form = ClienteProfileForm(request.POST, instance=perfil)
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            messages.success(request, "✅ Tu perfil ha sido actualizado correctamente")
            return redirect('mi_cuenta')
    else:
        user_form = UserForm(instance=user)
        perfil_form = ClienteProfileForm(instance=perfil)

    return render(request, 'core/mi_cuenta.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })