# Importamos el render para mostrar la plantilla HTML
from django.shortcuts import render

# Create your views here.

def saludo(request):
    return render(request, 'index.html', {})