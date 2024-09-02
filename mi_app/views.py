# views.py
from django.http import HttpResponse
from django.views import View

class MiVista(View):
    def get(self, request):
        return HttpResponse("¡Vista cargada correctamente!")

def index(request):
    return HttpResponse("¡Bienvenido a La Vitorina!")

