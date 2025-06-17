from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import custom_logout
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('add-cow/', views.add_cow, name='add_cow'),
    path('cow/<int:pk>/', views.cow_detail, name='cow_detail'),
    path('veterinarians/', views.vet_list, name='vet_list'),
    path('add-veterinarian/', views.add_vet, name='add_vet'),
    path('logout/', custom_logout, name='logout'),
]