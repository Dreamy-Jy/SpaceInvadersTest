from Ship import *
from random import *

ship = None #this will become the ship later on fam
lazers = []
def setup():
    global ship
    size(700,700)
    background(0)
    #setsup a horazontial lines
    ship = Ship(600,600) #sets up the ship

def draw():
    makeGrid()
    noFill()
    ship.show()
    renderLazers()

def renderLazers():
    global lazers
    for i in range(len(lazers)):
        lazers[i].drawType1()

def chackLazers():
    global lazer
    for i in range(len(lazers)):
        if lazers[i].y+lazers[i].objHeight < 0 or lazers[i].y - lazers[[]

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