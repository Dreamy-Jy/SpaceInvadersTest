class Ship():
    full_hp = 4
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 4
        self.is_damaged = False
        self.is_shooting = False
        self.is_moving = False
        self.is_live = True
        self.img = loadImage("Ship.png")
    
    def show(self):
        image(self.img, self.x, self.y)