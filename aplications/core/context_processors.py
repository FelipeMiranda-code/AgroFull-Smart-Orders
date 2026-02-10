def categorias(request):
    from .models import Categoria  # Importación dentro de la función
    return {"categorias_global": Categoria.objects.all()}


def carrito_count(request):
    carrito = request.session.get("carrito", {})
    total_items = sum(carrito.values())
    return {"carrito_count": total_items}
