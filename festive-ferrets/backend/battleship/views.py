from django.shortcuts import render
from battleship import battleshipCode
from battleship.models import gameMoves, gameSession
# Create your views here.

def home(request):
    return render(request, 'base.html')

def battleship(request):
    if "active" in request.GET:
        enemyMoves, playerMoves = battleshipCode.newGame()
        return render(request, 'battleship.html', {"playerMoves":playerMoves, "message":"These are where your battleships are positioned"})
        

    return render(request, 'battleship.html', {"startButton":"True"})