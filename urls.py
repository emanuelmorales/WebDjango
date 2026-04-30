from django.contrib import admin
from django.urls import path
from WebDjango import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.index, name='index'),
    path('usuarios/login/', view.login, name='login'),
    path('usuarios/salir/', view.salir, name='salir'),
    path('usuarios/registro/', view.registro, name='registro'),
]
 