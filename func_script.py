import character
import random


def setup_ai(len_player_units):
    ai_lis = []
    type_lis = ["w","t","w"]
    for i in range(len_player_units):
        ai_lis.append(character.GameCharacter(type_lis[random.randint(0,3)],"AI"+str(random.randint(10,100))))
    return ai_lis

def setup_player(num_unit):
    player_units = []
    for i in range(num_unit):

        player_unit_type = str(input('choose unit t / w / m = tanker / warrior / mage: '))
        player_unit_name = str(input("give your unit a name: "))
        player_units.append(character.GameCharacter(player_unit_type,player_unit_name))
    return player_units    