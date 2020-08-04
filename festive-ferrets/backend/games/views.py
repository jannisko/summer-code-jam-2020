from django.shortcuts import render
from games.models import liveGame, gameMoves

# Create your views here.

def home(request):
    return render(request, 'home.html')

def tictactoe(request):
    newGame, created = liveGame.objects.get_or_create(id=0,gameId="yes")
    
    movesModel, created2 = gameMoves.objects.get_or_create(game=newGame)
    moves = list(movesModel.moves)

    if "reset" in request.POST:
        movesModel.moves = "         "
        movesModel.save()
        moves = list(movesModel.moves)
        return render(request, 'tic-tac-toe.html', {"boardSetup":[0,1,2,3,4,5,6,7,8], "moves":moves})

    if "pos" in request.POST:

        player = movesModel.player
        pos = request.POST["pos"]
        try:
            pos = int(pos)
        except:
            return render(request, 'tic-tac-toe.html', {"boardSetup":[0,1,2,3,4,5,6,7,8],"error":"something went wrong :)","moves":moves,"player":player})
        
        if moves[pos] == " ":
            moves[pos] = movesModel.player
            movesModel.moves = "".join(moves)
            movesModel.save()
        else:
            return render(request, 'tic-tac-toe.html', {"boardSetup":[0,1,2,3,4,5,6,7,8],"error":"That square is taken!", "moves":moves,"player":player})

        victory = [False, " "]

        for x in [0, 3, 6]:
            if moves[x] == moves[x+1] and moves[x] == moves[x+2] and moves[x] != " ":
                victory = [True, moves[x]]

        for x in [0, 1, 2]:
            if moves[x] == moves[x+3] and moves[x] == moves[x+6] and moves[x] != " ":
                victory = [True, moves[x]]

        if moves[0] == moves[4] and moves[0] == moves[8] and moves[x] != " ":
            victory = [True, moves[x]]
        elif moves[2] == moves[4] and moves[2] == moves[6] and moves[x] != " ":
            victory = [True, moves[x]]

        if victory[0] == True:
            return render(request, 'tic-tac-toe.html', {"boardSetup":[0,1,2,3,4,5,6,7,8],"moves":moves,"error":"","player":player,"winner":victory[1]})

        if movesModel.player == "O":
            movesModel.player = "X"
            movesModel.save()
        elif movesModel.player == "X":
            movesModel.player = "O"
            movesModel.save()

        return render(request, 'tic-tac-toe.html', {"boardSetup":[0,1,2,3,4,5,6,7,8],"moves":moves,"error":"","player":player})
    else:   
        return render(request, 'tic-tac-toe.html', {"boardSetup":[0,1,2,3,4,5,6,7,8],"moves":moves,"error":"","player":player})

