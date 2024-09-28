from django.urls import path
from . import views

app_name = 'planes'  

urlpatterns = [
    path('', views.index, name='index'),  
    path('asignar_plan/<int:atleta_id>/', views.asignar_plan, name='asignar_plan'),
    path('list/', views.plan_list, name='plan_list'),
    path('create/', views.plan_create, name='plan_create'),
    path('<int:id>/', views.plan_detail, name='plan_detail'),  
    path('plan/update/<int:pk>/', views.plan_update, name='plan_update'),
    path('delete/<int:id>/', views.plan_delete, name='plan_delete'),
]
