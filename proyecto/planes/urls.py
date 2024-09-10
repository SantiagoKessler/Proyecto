# planes/urls.py
from django.urls import path
from . import views

app_name = 'planes'  # Este es el namespace que debes usar en las plantillas

urlpatterns = [
    path('', views.index, name='index'),  # Asegúrate de definir la vista 'index'
]
