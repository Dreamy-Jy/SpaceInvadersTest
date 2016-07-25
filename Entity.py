class Entity():
    is_damaged = False  # Adopt new variable assignment method 
    is_Live = True
    def __init__(self,x,y,hp):
        self.x = x
        self.y = y
        self.hp = hp
       