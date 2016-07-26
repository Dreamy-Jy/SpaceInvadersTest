from Entity import * 
from Lazer import *

class Ship(Entity):
    full_hp = 4
    
    def __init__(self, x, y):
        self.img = loadImage("Ship.png")
        super(Ship,self).__init__(x, y, Ship.full_hp, self.img.height, self.img.width)
        self.is_shooting = False
        self.is_moving = False
        #print("the height of this object is ",self.objHeight)
        #print("the width of this object is "+str(self.objWidth)+" and ship full hp is "+str(self.full_hp))
    
    def show(self):
        image(self.img, self.x, self.y)
    
    def shoot(self):
        return Lazer(self.x+ 25   ca, self.y + 3, 5, 1)