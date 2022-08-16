import random

class GameCharacter:
    def __init__(self,char_type,char_name):
        self.type = ""
        self.name = char_name
        self.hp = 100
        self.atk = 0
        self.df = 0
        self.exp = 0
        self.rk = 1

        if char_type == "w":
            self.setup_warrior()
        elif char_type == "t":
            self.setup_tanker()

def setup_warrior(self):
    self.type = "warrior"
    self.atk = random.randint(5,20)

def setup_tanker(self):
    self.type = "tanker"
    self.atk = random.randint(1,10)

def attack(self,target):
    damage = self.atk - target.df + random.randint(-5, 10)
    target.hp -= damage
       
