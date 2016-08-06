from Entity import * 
from Lazer import *

class Ship(Entity):
    full_hp = 6
    
    def __init__(self, x, y):
        self.img = loadImage("Ship.png")
        super(Ship,self).__init__(x, y, Ship.full_hp, self.img.height, self.img.width,"Ship")
        self.can_shoot = True
        self.is_moving = False

    def update(self):
        image(self.img, self.x, self.y)
    
    def shoot(self):
        if (self.can_shoot):
            return Lazer(self.x+ 25, self.y - 13, 5, 1)