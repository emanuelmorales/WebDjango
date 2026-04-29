# Importamos el render para mostrar la plantilla HTML
from django.shortcuts import render

# Create your views here.

def saludo(request):
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
        # print(request.method)
    if request.method == 'POST':
        # obtiene los datos enviados por el formulario mediante POST y con get se accede a ellos
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f'Username: {username}, Password: {password}')
    return render(request, 'users/login.html', {
        'mensaje':'Ingreso',
        'titulo':'Login',
    })