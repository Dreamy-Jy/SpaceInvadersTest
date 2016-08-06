from Ship import *
from Lazer import *
from random import *
from time import *
from Entity import *

"""
1. ALiens need to move 
2. bullet delay
3. wall line up
4. sounds
5. background
"""
lazers = []

# theirs going to be a method to load the list, this must be loaded in the setp method
entities = [
            [None],
            [None,None,None],
            [None,None,None,None,None,None,None,None,None,None,None,None,None,None]
            ]
'''
    ,None,None,None,None,
    None,None,None,None,None,None]'''
def setup():
    size(700,700)
    background(0)
    loadEntities()
    
def draw():
    global lazers, entities
    background(0)
    noFill()
    renderAllEntities()
    renderLazers()    
    checkLazers()
    checkForAlienFire()
    allObjForHit()
    checkIfObjDead()

def loadEntities():
    global entities
    
    # loads the ship
    entities[0][0] = Ship(600,600)
    
    # loads all walls
    startx = 100
    starty = 550
    for col in range(len(entities[1])):
        entities[1][col] = Wall(startx,starty)
        startx += 200
    
    # loads all of the aliens
    startx = 0
    starty = 100
    chx = 50
    chy = 0
    secondLine = True
    for col in range(len(entities[2])):
        entities[2][col] = Alien(startx, starty, 1)
        if (col+1)%11 == 0:
            chx = -1*startx +150
            starty += 100
        elif (col+1)%3 == 0:
            chx = 100
        else:
            chx = 50
        startx += chx
        starty += chy
    
    entities[2][12].x = 350 
    entities[2][13].x = 550
def updateAllEntities():
  pass  

def renderAllEntities():
    global entities
    for row in range(len(entities)):
        for col in range(len(entities[row])):
            if entities[row][col] != None and entities[row][col].is_Live:
                entities[row][col].update()

def renderLazers():
    global lazers
    for i in range(len(lazers)):
        lazers[i].drawType(lazers[i].type)

def allObjForHit():
    for row in range(len(entities)):
        for col in range(len(entities[row])):
            if entities[row][col] != None:
                checkIfLazersHit(entities[row][col])

def checkIfObjDead():
    global entities
    for row in range(len(entities)):
        for col in range(len(entities[row])):
            if entities[row][col] != None and entities[row][col].is_Live != True:
                entities[row][col] = None 

def checkForAlienFire():
    global entities, lazers
    for col in range(len(entities[2])):
        if entities[2][col] != None and entities[2][col].can_shoot:
            lazers.append(entities[2][col].shoot()) 
            
#made to test collision on the alien  
def checkIfLazersHit(obj):
    global lazers
    colL = 0     
    while colL < len(lazers):
        if obj.checkCollision(lazers[colL]):
            del lazers[colL]
            colL -= 1
            if colL < 0:
                colL += 1
        else:
            colL += 1




def checkLazers():
    global lazers, ship
    index = 0
    while index < len(lazers) :
        if lazers[index].y + lazers[index].objHeight < 0 or lazers[index].y > height:
            del lazers[index]
            index -= 1
            if index < 0:
                index += 1
        else:
            index += 1

     
def keyPressed():
    global entities,lazers
    
    if entities[0][0] != None:
        if key == "a" and entities[0][0].x > 0:
            entities[0][0].x -= 5
            return
        if key == "d" and entities[0][0].x < 700 - entities[0][0].objWidth:
            entities[0][0].x += 5
            return
        if key == " ":
            lazers.append(entities[0][0].shoot())
            return
    else:
        if key == "r":
            entities[0][0] = Ship(300,600)
            