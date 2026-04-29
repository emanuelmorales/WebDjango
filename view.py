# Importamos el render para mostrar la plantilla HTML
from django.shortcuts import redirect, render
# importar la libreria login (con alias lg) y auth para manejar la autenticacion de usuarios
from django.contrib.auth import login as lg
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import logout



# Create your views here.

def index(request):
    return render(request, 'index.html', {
        'mensaje':'Ingreso',
        'titulo':'Personas',
        'personas' : [
            {'titulo':'Maria','edad':'15','adulto':False},
            {'titulo':'Juan','edad':'20','adulto':True},
            {'titulo':'Ana','edad':'17','adulto':False},
            {'titulo':'Luis','edad':'25','adulto':True}
        ]
    })

def login(request):
    if request.method == 'POST':
        # con request obtiene los datos enviados por el formulario mediante POST y con get se accede a ellos
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # usuario contiene el resultado de la autenticacion, si es exitoso devuelve un objeto usuario, de lo contrario devuelve None
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            # lg es el alias de login importado, se le pasa el request y el usuario autenticado para iniciar la sesion
            lg(request, usuario)
            messages.success(request, f'Bienvenido {username}!')
            return redirect('index')  # redirige a la pagina de inicio despues de iniciar sesion
        else:
            messages.error(request, 'Credenciales inválidas')
            return render(request, 'users/login.html', {
                'mensaje':'Credenciales inválidas',
                'titulo':'Login',
            })  

    # En caso de que la solicitud no sea POST, se muestra el formulario de login
    return render(request, 'users/login.html', {
        'mensaje':'Ingreso',
        'titulo':'Login',
    })
    
def salir(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión')
    return redirect(login) 
    