from datetime import datetime
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
        self.atk = random.randint(17,20)
        self.df = random.randint(7,10)
        self.exp = 0
        
    def setup_tanker(self):
        self.type = "tanker"
        self.atk = random.randint(15,19)
        self.df = random.randint(9,10)
        self.exp = 0

    def setup_mage(self):
        self.type = "mage"
        self.atk = random.randint(19,25)
        self.df = random.randint(5,10)
        self.exp = 0

    

    def attack(self,target):
        # Getting the current date and time
        dt = datetime.now()

        damage = self.atk - target.df + random.randint(1, 10)
        exp = damage
        t_def = target.df 

       
        #bonus exp
        if damage >= 11:
            target.hp -= damage
            exp = damage*1.2
            self.exp += exp
            t_def = + (damage / 2)
            target.exp += t_def
           
        elif damage <= 10:
            target.hp -= damage
            exp = damage*1.5
            self.exp += exp
            t_def = + (damage / 2)
            target.exp += t_def
        

        #reset experince point 
        # and increase stats of units that level up  
        if self.exp >= 100 :
            self.exp -=100
            self.rk += 1
            self.atk += 5
            self.df += 5
        elif target.exp >= 100 :
            target.exp -= 100
            target.rk +=1
            target.atk += 5
            target.df += 5

        #update game log
        with open("game_log.txt","a")as f:
        
             f = f.write(self.name+" did "+str(damage)+" damage to "+target.name+"\n"+
             self.name+" gained "+str(exp)+"exp"+"\n"+str(target.name)+" gained "+str(t_def)+"exp from defending"+"\n"+str(dt)+"\n"+"\n")

        #print game state
        print(self.name+" did "+str(damage)+" damage to "+target.name)
        print(self.name+" gained "+str(exp)+"exp")
        print(str(target.name)+" gained "+str(t_def)+"exp from defending"+"\n")
        
        

    def __str__(self):
        text = self.type+" "+self.name+" "+"hp:"+str(self.hp)+"\n"
        text += "atk:" + str(self.atk)+" "+ "def:" + str(self.df)+ "\n"+"exp:"+str(self.exp)+" lvl:"+str(self.rk)+"\n"+"\n"
        return text 

    def get_damage(self):
        pass
        


