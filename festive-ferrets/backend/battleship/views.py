from django.shortcuts import render, redirect
from battleship import battleshipCode
from battleship.models import gameMoves, gameSession
# Create your views here.

def home(request):
    return render(request, 'base.html')

def battleship(request):
    if "active" in request.GET:
        if request.GET["active"] == "True":
            enemyShips, playerShips, id = battleshipCode.newGame()
            enemyShots, playerShots = battleshipCode.getShots(id)
            url = "/battleship/play?active="+str(id)
            return redirect(url)
        else:
            id = request.GET["active"]
            enemyShips, playerShips =battleshipCode.getBoard(id)
            enemyShots, playerShots = battleshipCode.getShots(id)
            if "enemyBeingShot" in request.POST:
                battleshipCode.writeShots(id, "player", request.POST["enemyBeingShot"])
                enemyShots, playerShots = battleshipCode.getShots(id)
        for x in enemyShips:
            print(x)

        return render(request, 'battleshipactive.html', {"playerShips":playerShips, "enemyShips":enemyShips,"playerShots":playerShots, "enemyShots":enemyShots, "message":"These are where your battleships are positioned"})
        

    return render(request, 'battleshipinactive.html', {"startButton":"True"})