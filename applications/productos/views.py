from django.views.generic import ListView
from .models import Producto, Categoria

class ProductoListView(ListView):
    model = Producto
    template_name = "productos/lista_productos.html"
    context_object_name = "productos"

    def get_queryset(self):
        queryset = Producto.objects.all()

        # Filtrado por búsqueda
        query = self.request.GET.get("buscar")
        if query:
            queryset = queryset.filter(nombre__icontains=query)

        # Filtrado por categoría si viene en la URL
        categoria_id = self.kwargs.get("pk")
        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        context["buscar"] = self.request.GET.get("buscar", "")

        # Nombre de la categoría actual
        categoria_id = self.kwargs.get("pk")
        if categoria_id:
            categoria = Categoria.objects.filter(pk=categoria_id).first()
            context["categoria_nombre"] = categoria.nombre if categoria else None
        else:
            context["categoria_nombre"] = None

        return context
