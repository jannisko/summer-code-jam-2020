from battleship.models import gameMoves, gameSession
from random import shuffle,randint

def getBoard(gameIdentifier):
    gameId = gameSession.objects.get(gameId=gameIdentifier)
    gameMoveModel = gameMoves.objects.get(game=gameId)

    enemyBoard = gameMoveModel.enemyMoves.split("-")

    for count,x in enumerate(enemyBoard):
        enemyBoard[count] = list(x)

    playerBoard = gameMoveModel.playerMoves.split("-")
    for count,x in enumerate(playerBoard):
        playerBoard[count] = list(x)
    return enemyBoard, playerBoard    

#############################################

def generateShipPos(enemy, player):
    for person in [enemy, player]:
        found = False
        while not found:
            y,x = randint(0,4) , randint(0,6)
            v = [1, -1]
            if y == 0:
                v = [1]
            if y == 4:
                v = [-1]
            try:
                if person[y][x] == " ":
                    shuffle(v)
                    try:
                        if person[y+v[0]][x]==" ":
                            person[y][x] = "O"
                            person[y+v[0]][x] = "O"
                            found = True
                    except:
                        try:
                            if person[y+v[1]][x]==" ":
                                person[y][x] = "O"
                                person[y+v[1]][x] = "O"
                                found = True
                        except:
                            pass
            except:
                pass
            
        found = False
        while not found:
            y,x = randint(0,4) , randint(0,6)
            v = [1, -1]
            if x == 0:
                v = [1]
            if x == 6:
                v = [-1]
            try:
                if person[y][x] == " ":
                    shuffle(v)
                    try:
                        if person[y][x+v[0]]==" ":
                            person[y][x] = "O"
                            person[y][x+v[0]] = "O"
                            found = True
                    except:
                        try:
                            if person[y][x+v[1]]==" ":
                                person[y][x] = "O"
                                person[y][x+v[1]] = "O"
                                found = True
                        except:
                            pass
            except:
                pass

    return enemy, player

######################################

def newGame():
    gameId, created = gameSession.objects.get_or_create(gameId="battleship")
    gameMoveModel, created = gameMoves.objects.get_or_create(game=gameId)

    enemyBoard, playerBoard = getBoard(gameId.gameId)
    enemyBoard, playerBoard = generateShipPos(enemyBoard, playerBoard)

    return enemyBoard, playerBoard