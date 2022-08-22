
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
        else:
            self.setup_mage()
    
    # setting up units
    def setup_warrior(self):
        self.type = "warrior"
        self.atk = random.randint(5,20)
        self.df = random.randint(1,10)
        self.exp = 0
        
    def setup_tanker(self):
        self.type = "tanker"
        self.atk = random.randint(1,10)
        self.df = random.randint(5,15)
        self.exp = 0

    def setup_mage(self):
        self.type = "mage"
        self.atk = random.randint(20,30)
        self.df = random.randint(1,5)
        self.exp = 0

    def attack(self,target):
        damage = self.atk - target.df + random.randint(-5, 10)
        # TODONE: implement fix for negative damage
        if damage >= 1:
            target.hp -= damage
        else:
            target.hp -= 1    
        print(self.name+" did "+str(damage)+" damage")
        
        

    def __str__(self):
        text = self.type+" "+self.name+",hp:"+str(self.hp)
        text += ", atk:" + str(self.atk)+", df" + str(self.df)
        return text   

    def get_damage(self):
        pass
        

