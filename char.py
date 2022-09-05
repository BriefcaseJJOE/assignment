import random

class GameCharacter:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        # SET CUSTOM ATK,DEF,EXP 
    
    def attack(self, other):
        # randomly choose attack amount
        damage = self.atk - other.df + random.randint(-5, 10)
        if damage <= 0:
            damage = 1
        
        # inflict on other
        other.hp =- damage
    

    def __str__(self):
        representation = self.name + '\n'
        representation += '~' * 30 + '\n'
        representation += 'atk : ' + str(self.atk) + '\n'
        representation += 'def : ' + str(self.df) + '\n'
        representation += 'exp : ' + str(self.exp) + '\n'

        return representation



class Mage(GameCharacter):
    def __init__(self, name):
        self.atk = random.randint(19,25)
        self.df = random.randint(5,10)
        self.exp = 0

        super().__init__(name)


class Mage(GameCharacter):
    def __init__(self, name):
        self.atk = random.randint(19,25)
        self.df = random.randint(5,10)
        self.exp = 0

        super().__init__(name)


class Mage(GameCharacter):
    def __init__(self, name):
        self.atk = random.randint(19,25)
        self.df = random.randint(5,10)
        self.exp = 0

        super().__init__(name)
    

if __name__ == '__main__':
    my_char = Mage('zy')


    print(my_char)