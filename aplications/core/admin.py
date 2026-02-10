from django.contrib import admin
from .models import ClienteProfile, Producto,Categoria

admin.site.register(Producto)
admin.site.register(Categoria)

class ClienteProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre_empresa',
        'rut',
        'telefono',
        'direccion',
    )
    search_fields = ('nombre_empresa', 'rut')
    list_filter = ('nombre_empresa',)
admin.site.register(ClienteProfile, ClienteProfileAdmin)
