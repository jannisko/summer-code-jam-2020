from django import template

register = template.Library()

########filters############
def lookup(array, key):
    key = int(key)
    return array[key]


########simple tags########
def returnInfo(key, key2, playerShots, enemyShips):

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

register.filter(lookup)
register.simple_tag(returnInfo)