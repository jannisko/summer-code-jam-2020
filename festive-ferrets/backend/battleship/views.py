from django.shortcuts import render, redirect
from battleship import battleshipCode
from battleship.models import gameMoves, gameSession
# Create your views here.

def home(request):
    return render(request, 'base.html')

def battleship(request):
    message = "Welcome to battleship!"
    if "reset" in request.POST:
        battleshipCode.deleteGame(request.GET["active"])
        return redirect("/battleship/play")
    elif "active" in request.GET:
        if request.GET["active"] == "True":
            enemyShips, playerShips, id = battleshipCode.newGame()
            enemyShots, playerShots = battleshipCode.getShots(id)
            url = "/battleship/play?active="+str(id)
            return redirect(url)
        else:
            id = request.GET["active"]
            turn, message = battleshipCode.getTurn(id)
            enemyShips, playerShips =battleshipCode.getBoard(id)
            enemyShots, playerShots = battleshipCode.getShots(id)
            if "enemyBeingShot" in request.POST:
                battleshipCode.writeShots(id, "player", request.POST["enemyBeingShot"])
                enemyShots, playerShots = battleshipCode.getShots(id)
                battleshipCode.enemyTurn(id)
                turn, message = battleshipCode.getTurn(id)


        return render(request, 'battleshipactive.html', {"playerShips":playerShips, "enemyShips":enemyShips,"playerShots":playerShots, "enemyShots":enemyShots, "message":message, \
            "resetButton":"True", "turn":turn})
        

    return render(request, 'battleshipinactive.html', {"startButton":"True"})