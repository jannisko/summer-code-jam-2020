from django.urls import path,re_path
from tictactoe import views

urlpatterns = [
    path('', views.home),
    path('play/', views.tictactoe),
]