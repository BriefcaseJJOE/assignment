
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
        elif char_type == "dev":
            self.setup_devil()
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

    def setup_devil(self):
        self.type = "dev"
        self.atk = random.randint(80,99)
        self.df = random.randint(29,30)
        self.exp = 0

    def attack(self,target):
        damage = self.atk - target.df + random.randint(-5, 10)
        # TODONE: implement fix for negative damage
        exp = damage
        
        t_def = target.df 
      
        if damage <= 0:
            damage = 1 
            exp = damage
            self.exp += exp
            target.exp += t_def
          
            
        else:
            target.hp -= damage
            self.exp += exp
            target.exp += t_def
            
        if self.exp >= 100 :
            self.exp -=100
            self.rk +=1
        elif target.exp >= 100 :
            target.exp -= 100
            target.rk +=1
          
        print(self.name+" did "+str(damage)+" damage to "+target.name)
        print(self.name+" gained "+str(exp)+"exp")
        print(str(target.name)+" gained "+str(t_def)+"exp from defending"+"\n")
        
        

    def __str__(self):
        text = self.type+" "+self.name+" "+"hp:"+str(self.hp)+"\n"
        text += "atk:" + str(self.atk)+" "+ "def:" + str(self.df)+ "\n"+"exp:"+str(self.exp)+" lvl:"+str(self.rk)+"\n"+"\n"
        return text 

    def get_damage(self):
        pass
        

