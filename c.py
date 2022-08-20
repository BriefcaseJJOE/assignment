
import random

def setup_ai(len_player_units):
    ai_lis = []
    type_lis = ["w","t","w"]
    for i in range(len_player_units):
        ai_lis.append(GameCharacter(type_lis[random.randint(0,3)],"AI"+str(random.randint(10,100))))
    return ai_lis

def setup_player(num_unit):
    player_units = []
    for i in range(num_unit):

        player_unit_type = str(input('choose unit t / w / m = tanker / warrior / mage: '))
        player_unit_name = str(input("give your unit a name: "))
        player_units.append(c.GameCharacter(player_unit_type,player_unit_name))
    return player_units    

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
    

    def setup_warrior(self):
        self.type = "warrior"
        self.atk = random.randint(5,20)
        self.df = random.randint(1,10)
        
    def get_attack(self):
        return self.atk

    def setup_tanker(self):
        self.type = "tanker"
        self.atk = random.randint(1,10)
        self.df = random.randint(5,15)
        


    def setup_mage(self):
        self.type = "mage"
        self.atk = random.randint(5,30)
        self.df = random.randint(1,5)
        

    def attack(self,target):
        damage = self.atk - target.df + random.randint(-5, 10)
        target.hp -= damage

    def __str__(self):
        text = self.type+" "+self.name+",hp:"+str(self.hp)
        text += ", atk:" + str(self.atk)+", df" + str(self.df)
        return text   




    '''out put list of 
        ai units == player units
        ai units will be selected randomly
        ai name prefix "AI(two digit)"

    '''


