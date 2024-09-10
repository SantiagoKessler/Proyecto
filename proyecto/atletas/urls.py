from django.urls import path
from . import views

app_name = "atletas"

urlpatterns = [
   path("", views.index, name = "index"),
   path("pais/list", views.pais_list, name = "pais_list"),
   path("pais/create", views.pais_create, name = "pais_create"),
]
