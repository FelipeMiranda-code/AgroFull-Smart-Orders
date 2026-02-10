from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('direcciones/', views.lista_direcciones, name='lista_direcciones'),
    path('direcciones/nueva/', views.crear_direccion, name='crear_direccion'),
    path('direcciones/<int:pk>/editar/', views.editar_direccion, name='editar_direccion'),
    path('direcciones/<int:pk>/borrar/', views.borrar_direccion, name='borrar_direccion'),
    path('perfil/', views.perfil, name='perfil'),

]
