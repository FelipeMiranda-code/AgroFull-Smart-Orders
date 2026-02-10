from django.db import models

from django.contrib.auth.models import User
from applications.productos.models import Producto

class Pedido(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmado', 'Confirmado'),
        ('enviado', 'Enviado'),
        ('cancelado', 'Cancelado'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    direccion = models.ForeignKey(
    'usuarios.Direccion',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='pedidos'
    )

    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username}"

    @property
    def total(self):
        detalles = self.detallepedido_set.all()
        return sum([item.subtotal for item in detalles])


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.producto.nombre} ({self.cantidad})"

    @property
    def subtotal(self):
        return self.cantidad
