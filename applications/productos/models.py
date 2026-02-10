from django.db import models

class Categoria(models.Model):
    nombre = models.CharField('Nombre', max_length=50)

    class Meta:
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre
    

class Producto(models.Model):

    UNIDAD_OPCIONES = (
        ("Kilo", "Kilo"),
        ("Unidad", "Unidad"),
    )

    nombre = models.CharField('Nombre', max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos")
    unidad = models.CharField('Unidad', max_length=10, choices=UNIDAD_OPCIONES)
    imagen = models.ImageField(upload_to="productos/", blank=True, null=True)
    
    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
