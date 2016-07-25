class Entity():
    is_damaged = False  # Adopt new variable assignment method 
    
    def __init__(self,x,y,hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.is_Damaged = False
        self.is_Live = True