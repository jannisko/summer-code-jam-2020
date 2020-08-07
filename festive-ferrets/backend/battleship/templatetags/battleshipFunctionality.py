from django import template

register = template.Library()

########filters############
def lookup(array, key):
    key = int(key)
    return array[key]


########simple tags########
def returnInfoE(key, key2, playerShots, enemyShips):

    for x in playerShots[1:]:
        try:
            
            if x[0] == str(key2):
                if x[1] == str(key):
                    if enemyShips[key2][key] == "O":
                        return "hit"
                    else:
                        return "miss"
            else:
                continue
        except:
            return False

    return False

def returnInfoP(key, key2, enemyShots, playerShips):

    for x in enemyShots[1:]:
        try:
            
            if x[0] == str(key2):
                if x[1] == str(key):
                    if playerShips[key2][key] == "O":
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