from django.urls import path
from . import views

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
]