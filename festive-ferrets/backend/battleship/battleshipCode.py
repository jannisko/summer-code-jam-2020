from battleship.models import gameMoves, gameSession
from random import shuffle,randint

def deleteGame(gameIdentifier):
    try:
        gameId = gameSession.objects.get(gameId=gameIdentifier)
        gameMoves.objects.get(game=gameId).delete()
        gameId.delete()
    except:
        pass


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


def writeBoard(enemyBoard, playerBoard, gameIdentifier):
    gameId = gameSession.objects.get(gameId=gameIdentifier)
    gameMoveModel = gameMoves.objects.get(game=gameId)

    modelFriendly = ""
    for x in enemyBoard:
        for area in x:
            modelFriendly+=area
        modelFriendly+="-"
    gameMoveModel.enemyMoves = modelFriendly[0:len(modelFriendly)-1]
    gameMoveModel.save()

    modelFriendly = ""
    for x in playerBoard:
        for area in x:
            modelFriendly+=area
        modelFriendly+="-"
    gameMoveModel.playerMoves = modelFriendly[0:len(modelFriendly)-1]
    gameMoveModel.save()
    



########################

def getShots(gameIdentifier):
    gameId = gameSession.objects.get(gameId=gameIdentifier)
    gameMoveModel = gameMoves.objects.get(game=gameId)

    enemyShots = gameMoveModel.enemyShots.split("-")
    playerShots = gameMoveModel.playerShots.split("-")

    return enemyShots, playerShots 

def writeShots(gameIdentifier, person, shot):
    gameId = gameSession.objects.get(gameId=gameIdentifier)
    gameMoveModel = gameMoves.objects.get(game=gameId)
    
    if person == "player":
        gameMoveModel.playerShots = gameMoveModel.playerShots +"-"+ str(shot)
        gameMoveModel.save()
    elif person == "enemy":
        gameMoveModel.enemyShots = gameMoveModel.enemyShots +"-"+ str(shot)
        gameMoveModel.save()
        
#############################

def getTurn(id):
    gameId = gameSession.objects.get(gameId=id)
    gameMoveModel = gameMoves.objects.get(game=gameId)

    turn = gameMoveModel.turn
    if turn == "p":
        gameMoveModel.turn = "e"
        message = "It is your turn"
        gameMoveModel.save()
    elif turn == "e":
        gameMoveModel.turn = "p"
        message = "It is the enemies turn"
        gameMoveModel.save()

    return turn, message


######################################

def newGame():
    gameId, created = gameSession.objects.get_or_create(gameId="battleship")
    gameMoveModel, created = gameMoves.objects.get_or_create(game=gameId)

    enemyBoard, playerBoard = getBoard(gameId.gameId)
    enemyBoard, playerBoard = generateShipPos(enemyBoard, playerBoard)
    writeBoard(enemyBoard, playerBoard, gameId.gameId)


    return enemyBoard, playerBoard, gameId.gameId

    ################

def enemyTurn(id):
    p, e = getShots(id)
    found = False
    while not found:
        shot = str(randint(0,4))+str(randint(0,6))
        if shot in e:
            continue
        else:
            found=True
    writeShots(id, "enemy", shot)

#### 

def hitCount(id,person, shot):
    gameId = gameSession.objects.get(gameId=id)
    gameMoveModel = gameMoves.objects.get(game=gameId)

    print(id,person,shot,gameMoveModel.eSunk,"tt",gameMoveModel.pSunk)
    if person == "e":
        if shot in gameMoveModel.eSunk:
            return None
        else:
            gameMoveModel.eSunk+= "-"+shot

    elif person == "p":
        if shot in gameMoveModel.pSunk:
            return None
        else:
            gameMoveModel.pSunk+= "-"+shot

    gameMoveModel.save()

    
def victoryCheck(id):
    gameId = gameSession.objects.get(gameId=id)
    gameMoveModel = gameMoves.objects.get(game=gameId)   
    print(len(gameMoveModel.eSunk.split("-")) == 5)
    if len(gameMoveModel.eSunk.split("-")) == 5:
        return "p"
    elif len(gameMoveModel.pSunk.split("-")) == 5:
        return "e"

    return False

