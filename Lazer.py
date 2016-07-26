from random import *

class Lazer(object):
    def __init__(self, x, y, speed, type):
        self.x = x
        self.y = y
        self.speed = speed
        self.type = type
        
    def drawType1(self):
        fill(randint(0,255),randint(0,255),randint(0,255))
        ellipse(self.x, self.y, 10, 10)
        self.y -= self. speed
    def drawType2(self):
        fill(randint(0,255),randint(0,255),randint(0,255))
        ellipse(self.x, self.y, 5, 50)
        self.y += self.speed