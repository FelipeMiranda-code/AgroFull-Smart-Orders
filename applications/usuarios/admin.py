from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Direccion

# -------------------------------
# ADMIN DE USUARIOS
# -------------------------------

# Primero desregistramos el User original
admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

# -------------------------------
# ADMIN DE DIRECCIONES
# -------------------------------

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'calle', 'numero', 'comuna', 'principal')
    list_filter = ('comuna', 'principal')
    search_fields = ('usuario__username', 'calle', 'comuna')
