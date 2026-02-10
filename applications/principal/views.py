from django.shortcuts import render

from django.views.generic import TemplateView

class InicioView(TemplateView):
    template_name = 'principal/inicio.html'

def nosotros(request):
    return render(request, 'principal/nosotros.html')
