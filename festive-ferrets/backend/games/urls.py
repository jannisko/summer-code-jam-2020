from django.urls import path,re_path
from games import views

urlpatterns = [
    path('home', views.home),
    path('tic-tac-toe', views.tictactoe),
]