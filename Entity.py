class Entity(object):
    is_damaged = False  # Adopt new variable assignment method 
    is_Live = True
    def __init__(self, x, y, hp, objHeight, objWidth):
        self.x = x
        self.y = y
        self.hp = hp
        self.objHeight = objHeight
        self.objWidth = objWidth
        self.is_damaged = False
        self.is_live = True
        self.currentHpBar = None #will become the img programs current hp bar will change when hit
    
    # I want to set this so the is damaged is ran it the decrHp method but i don't want this to check every time
    def decrHp(self, downBy):
        self.hp -= downBy
        print(str(self.hp)+" is my new hp")
        if self.hp == 0:
            print('im dead')
            
    # will display the current hp bar
    def desplayHpBar(self):
        pass
    
    #will respond to colisions
    def hit(self):
        pass
    #will respond to death mean to be overriden
    def die(self):
        pass