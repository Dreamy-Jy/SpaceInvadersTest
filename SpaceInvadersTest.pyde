from Ship import *
from Lazer import *
from random import *
from time import *

ship = None #this will become the ship later on fam
alien = None
lazers = []

# theirs going to be a method to load the list, this must be loaded in the setp method
entities = [
            [ship],
            [alien]
            ]

def setup():
    global ship, alien
    size(700,700)
    background(0)
    #setsup a horazontial lines
    ship = Ship(600,600) #sets up the ship
    alien = Alien(300,300,1)
    entities[0][0] = ship
    entities[1][0] = alien
    
def draw():
    global ship,alien, lazers, entities
    makeGrid()
    noFill()
    #entities[0][0].update()
    #entities[1][0].update()
    renderAllEntities()
    renderLazers()
    checkLazers()
    allObjForHit()

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
        lazers[i].drawType1()

def allObjForHit():
    for row in range(len(entities)):
        for col in range(len(entities[row])):
            if entities[row][col] != None:
                checkIfLazersHit(entities[row][col])

#made to test collision on the alien  
def checkIfLazersHit(obj):
    global lazers
    print("checking for hits")
    colL = 0     
    while colL < len(lazers):
        if obj.checkCollision(lazers[colL]):
            del lazers[colL]
            colL -= 1
            if colL < 0:
                colL += 1
        else:
            colL += 1

# maybe we can just chack the frist lazer in the list and see if we need to remove it and the other lazers next
#coonsider reversing the if statment to look if the lazer is in the screen
#this makes the function go out for bounds
def checkLazers():
    global lazers, ship
    #everyoneStopShooting()
    index = 0
    while index < len(lazers) :
        if lazers[index].y + lazers[index].objHeight < 0 or lazers[index].y > height:
            del lazers[index]
            index -= 1
            if index < 0:
                index += 1
        else:
            index += 1

'''everyoneStopShooting()
this method prevents all entities from shooting because the way system works is
that two thread running in the program that involve them selfs with lazer creation
the draw() renders the lazers to the screen and checks if the lazer have left the screen
or hit something, so if an of those two happen in can take the lazer out of the game. 
The second thread the keyPressed() created new bullet when the draw() was checking the
list causing concurrency 
''' # may not be needed
def everyoneStopShooting():
    global ship
    ship.can_shoot = False
# may not be needed
def everyoneStartShooting():
    global ship
    ship.can_shoot = True

#will destroy
def makeGrid():
    background(255)
    fill(255,255,255)
    x1 = 0
    x2 = 700
    y = 0
    for i in range(14):
        line(x1,y,x2,y)
        y += 50
    x = 0
    y1 = 0
    y2 = 700
    for i in range(14):
        line (x,y1,x,y2)
        x += 50
     
def keyPressed():
    global ship,lazers
    if key == "a" and ship.x > 0:
        ship.x -= 5
        return
    if key == "d" and ship.x < 700 - ship.objWidth:
        ship.x += 5
        return
    if key == " ":
        lazers.append(ship.shoot())
        return