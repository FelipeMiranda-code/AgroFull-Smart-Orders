from django.urls import path
from .views import (
    HomeView, CustomLoginView, RegistroView, RegistroClienteView, DashboardView,
    lista_productos, cerrar_sesion, agregar_al_carrito,
    ver_carrito, eliminar_item, checkout, productos_por_categoria,
    detalle_producto,mi_cuenta
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", cerrar_sesion, name="logout"),
    path("registro/", RegistroView.as_view(), name="registro"),
    path("registro/cliente/", RegistroClienteView.as_view(), name="registro_cliente"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("productos/", lista_productos, name="productos"),
    path("agregar/<int:producto_id>/", agregar_al_carrito, name="agregar_carrito"),
    path("carrito/", ver_carrito, name="carrito"),
    path("carrito/eliminar/<int:producto_id>/", eliminar_item, name="eliminar_item"),
    path("checkout/", checkout, name="checkout"),
    path("categoria/<int:categoria_id>/", productos_por_categoria, name="categoria"),
    path("producto/<int:producto_id>/", detalle_producto, name="detalle_producto"),
    path('mi_cuenta/', mi_cuenta, name='mi_cuenta'),
]
