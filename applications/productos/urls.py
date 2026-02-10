from django.urls import path
from .views import ProductoListView

urlpatterns = [
    path("", ProductoListView.as_view(), name="lista_productos"),
    path("categoria/<int:pk>/", ProductoListView.as_view(), name="productos_por_categoria"),
]
