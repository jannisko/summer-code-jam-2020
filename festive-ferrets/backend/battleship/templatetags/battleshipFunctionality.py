from django import template
from battleship.battleshipCode import hitCount
register = template.Library()

########filters############
def lookup(array, key):
    key = int(key)
    return array[key]


########simple tags########
def returnInfoE(key, key2, playerShots, enemyShips, id):
    for x in playerShots[1:]:
        try:
            
            if x[0] == str(key2):
                if x[1] == str(key):
                    if enemyShips[key2][key] == "O":
                        hitCount(id, "e",str(key2)+str(key))
                        return "hit"
                        
                    else:
                        return "miss"
            else:
                continue
        except:
            return False

    return False

def returnInfoP(key, key2, enemyShots, playerShips, id):

    for x in enemyShots[1:]:
        try:
            if x[0] == str(key2):
                if x[1] == str(key):
                    if playerShips[key2][key] == "O":
                        hitCount(id, "p",str(key2)+str(key))
                        return "hit"
                        
                    else:
                        return "miss"

            else:
                continue
        except:
            return False

    return False

register.filter(lookup)
register.simple_tag(returnInfoE)
register.simple_tag(returnInfoP)