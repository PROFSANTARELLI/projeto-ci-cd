class Player: 
    def __init__(self, name, hp): 
        self.name = name 
        self.hp = hps
 
    def take_damage(self, amount): 
        self.hp -= amount 
        if self.hp < 0: 
            self.hp = 0
