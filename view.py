from django.http import HttpResponse

# Create your views here.

def saludo(request):
    return HttpResponse("Hola Mundo, te saludo desde mi fucion de Django")