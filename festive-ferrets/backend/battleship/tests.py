from django.test import TestCase
from random import shuffle, randint
# Create your tests here.
person = []
for x in range(5):
    person.append([" "," "," "," "," "," "," "])
for x in person:
    print(x)

found = False
while not found:
    y,x = randint(0,4) , randint(0,6)
    v = [1, -1]
    print(y,x)
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

print("")
for x in person:
    print(x)