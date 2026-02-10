from django.db import models
from django.contrib.auth.models import User

class Direccion(models.Model):
    usuario = models.ForeignKey(User, related_name="direcciones", on_delete=models.CASCADE)

    nombre = models.CharField(max_length=100)  # Ej: "Casa", "Trabajo"
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)
    comuna = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    referencia = models.TextField(blank=True, null=True)

    principal = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} - {self.calle} {self.numero}, {self.comuna}"
