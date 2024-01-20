from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home page'),
    path('room/', views.room, name='room page'),
    
]