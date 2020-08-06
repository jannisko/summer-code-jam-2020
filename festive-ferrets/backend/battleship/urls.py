from django.urls import path
from battleship import views

urlpatterns = [
    path('', views.home),
    path('play/', views.battleship),
]