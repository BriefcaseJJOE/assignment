import character
import random


def setup_ai(len_player_units):
    ai_lis = []
    type_lis = ["w","t","m"]
    for i in range(len_player_units):
        ai_lis.append(character.GameCharacter(type_lis[random.randint(0,2)],"AI" + str(random.randint(0,9)) + str(random.randint(0,9) )))
    return ai_lis

def setup_player(num_unit):
    player_units = []
    for i in range(num_unit):

        player_unit_type = str(input('choose unit '+str(i+1)+' t / w / m = tanker / warrior / mage: '))
        player_unit_name = str(input("give your unit a name: "))
        player_units.append(character.GameCharacter(player_unit_type,player_unit_name))
    return player_units    

def update_player_units(number_of_player_unit,player_units):
    for i in range(number_of_player_unit):
            print(player_units[i].__str__(),end=" / ")

def update_ai_units(number_of_ai_unit,ai_units):
    for i in range(number_of_ai_unit):
            print(ai_units[i].__str__(),end=" / ")


def clear_screen():
    print("\n"*10)


def show_game_board(player_units,ai_units):
    print("Player unit")
    update_player_units(len(player_units),player_units)
    print("\n")
    print("Ai units")
    update_ai_units(len(ai_units),ai_units)
    print("\n")

def check_hp_is_zero(units):
   
    for i in range(len(units)):
        hp = units[i].hp
        if hp <= 0:
            return True

def dead_unit_index(units):
   
    for i in range(len(units)):
        hp = units[i].hp
        if hp <= 0:
            return i



    
