from Lazer import *
from random import *

class Entity(object):
    is_damaged = False  # Adopt new variable assignment method 
    is_Live = True
    def __init__(self, x, y, hp, objHeight, objWidth):
        self.x = x
        self.y = y
        self.hp = hp
        self.objHeight = objHeight
        self.objWidth = objWidth
        #self.is_damaged = False
        #self.is_live = True
        #self.currentHpBar = None #will become the img programs current hp bar will change when hit
    
    # I want to set this so the is damaged is ran it the decrHp method but i don't want this to check every time
    def decrHp(self, downBy):
        self.hp -= downBy
        print(str(self.hp)+" is my new hp")
        if self.hp == 0:
            self.is_Live = False
        
    # will display the current hp bar
    def desplayHpBar(self):
        pass
    
    #will respond to colisions
    def checkCollision(self, obj):
        if (self.x <= obj.x and self.x + self.objWidth >= obj.x) and (self.y <= obj.y and self.y + self.objHeight >= obj.y):
            self.decrHp(1)
            return True
        return False

    #will respond to death mean to be overriden
    def die(self):
        pass
#--------------------------------------------------------------------------------------------#
class  Alien(Entity):
    full_hp = 4
    def __init__(self, x, y, type):
        self.imgs = [loadImage("Alien"+str(type)+"pic1.png"),loadImage("Alien"+str(type)+"pic2.png"),loadImage("Alien"+str(type)+"pic3.png")]
        super(Alien,self).__init__(x, y, Alien.full_hp, self.imgs[0].height, self.imgs[0].width)
        self.openOrClose = True
        self.chance_to_shoot = randint(100,300)

    def update(self):
        image(self.imgs[second()%2], self.x+1, self.y)
        if second()%2 == 0:
            self.openOrClose = True
        else:
            self.openOrClose = False
        """
        if second()% == False and randint(1,3000)%self.chance_to_shoot == 0:
            print("alien can shoot")
            image(self.imgs[2], self.x+1, self.y)
        """