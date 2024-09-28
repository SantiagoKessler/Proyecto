
from django.urls import path
from . import views

app_name = "atletas"

urlpatterns = [
    path("", views.index, name = "index"),
    path("pais/list", views.PaisList.as_view(), name = "pais_list"),
    path("pais/create", views.PaisCreate.as_view(), name = "pais_create"),
    path('atleta/detail/<int:pk>/',views.PaisDetail.as_view(),name='atleta_detail',), 
    path('atleta/update/<int:pk>/',views.PaisUpdate.as_view(),name='atleta_update',),
    path( 'atleta/delete/<int:pk>/', views.PaisDelete.as_view(), name='atleta_delete')
]
