# mi_app/urls.py
from django.urls import path
from .views import MiVista, index  # Importa correctamente ahora

urlpatterns = [
    path('', index, name='index'),
    path('api/mensaje/', MiVista.as_view(), name='mensaje'),
]
