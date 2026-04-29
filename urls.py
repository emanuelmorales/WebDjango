from django.contrib import admin
from django.urls import path
from WebDjango import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.saludo, name='saludo'),
    path('usuarios/login/', view.login, name='login'),
]
 