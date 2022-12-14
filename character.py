import random

# logging
import logging
import logging.handlers
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.handlers.RotatingFileHandler('./game_log.txt')
formatter = logging.Formatter('%(asctime)s : %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)



class GameCharacter:
    def __init__(self,char_type,char_name,belongs_to=''):
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

        if belongs_to == 'player':
            logger.info('player set up ' + char_type.upper() + ' type character "' + char_name + '"')
        else:
            logger.info('AI set up ' + char_type.upper() + ' type character "' + char_name + '"')
        logger.info('(' + char_name + ') atk : ' + str(self.atk))
        logger.info('(' + char_name + ') df : ' + str(self.df))
        logger.info('(' + char_name + ') exp : ' + str(self.exp))
    
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
        damage = self.atk - target.df + random.randint(1, 10)
        exp = damage
        t_def = target.df 
        coin = 0
        

        #bonus exp and coins
        if damage >= 11:
            #damage
            target.hp -= damage
            #bonus exp 
            exp = damage*1.2
            self.exp += exp
            #exp from def
            t_def = + (damage / 2)
            target.exp += t_def
            #coins
            coin = exp
        elif damage <= 10:
            #damage
            target.hp -= damage
            #bonus exp 
            exp = damage*1.5
            self.exp += exp
            #exp from def
            t_def = + (damage / 2)
            target.exp += t_def
            #coins
            coin = exp
        #for negative health
        if target.hp <=0:
            target.hp = 0

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
        logger.info(self.name + " did " + str(damage) + " damage to " + target.name)
        logger.info(self.name + " gained " + str("{:.0f}".format(exp)) + "exp")
        logger.info(str(target.name) + " gained " + str("{:.0f}".format(t_def)) + "exp from defending")

        #print game state
        print(self.name+" did "+str(damage)+" damage to "+target.name)
        print(self.name+" gained "+str("{:.0f}".format(exp))+"exp")
        print(str(target.name)+" gained "+str("{:.0f}".format(t_def))+"exp from defending"+"\n")
        
        
        

    def __str__(self):
        text = self.type+" "+self.name+" "+"hp:"+str("{:.0f}".format(self.hp))+"\n"
        text += "atk:" + str(self.atk)+" "+ "def:" + str(self.df)+ "\n"+"exp:"+str("{:.0f}".format(self.exp))+" lvl:"+str(self.rk)+"\n"
        return text 

    
        


