from Ship import *

ship = 0
def setup():
    global ship
    size(700,700)
    background(0)
    #setsup a horazontial lines
    ship = Ship(600,600)


def draw():
    makeGrid()
    noFill()
    ship.show()

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
    global ship
    if key == "a":
        ship.x -= 5
    if key == "d":
        ship.x += 5