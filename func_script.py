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

        player_unit_type = roles_checker()
        player_unit_name = str(input("give your unit a name: "))
        player_units.append(character.GameCharacter(player_unit_type,player_unit_name,belongs_to='player'))
    return player_units    

def update_player_units(number_of_player_unit,player_units):
    for i in range(number_of_player_unit):
            print(player_units[i].__str__(),end=" ")

def update_ai_units(number_of_ai_unit,ai_units):
    for i in range(number_of_ai_unit):
            print(ai_units[i].__str__(),end=" ")


def clear_screen():
    print("\n"*30)


def show_game_board(player_units,ai_units):
    print("@@@( Player unit )@@@")
    update_player_units(len(player_units),player_units)
    print("\n")
    print("@@@( Ai unit )@@@")
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


def get_high_atk_unit(list):
    high = 0
    index_of_unit = 0
    for i in range(len(list)):
        if high < list[i].atk:
            high = list[i].atk
            index_of_unit = i
    return index_of_unit


def unit_checker():
    answer = ""
    while isinstance(answer, int) == False:
        try:
            answer = int(input("select number of units capped at 3: "))
            if answer > 3 :
                answer = 3
                print("selected more than 3 defaulted to 3 units")  
            elif answer < 1 :
                answer = 1 
                print("selected less than 1 defaulted to 1 unit")   
            return answer
        
        except:     
            print("input error try again!")

def input_checker_int_select():
    answer = ""
    while isinstance(answer, int) == False:
        try:
            answer = int(input("select unit to attack (1 for 1st unit, 2 for 2nd unit etc...: ") )
            return answer
        
        except:     
            print("input error try again!")


def input_checker_int_atk():
    answer = ""
    while isinstance(answer, int) == False:
        try:
            answer = int(input("select ai_unit to attack (1 for 1st unit, 2 for 2nd unit etc...: "))
            return answer
        
        except:     
            print("input error try again!")

def roles_checker():
    answer = ""
    while True:
        
        answer = str(input('choose unit t / w / m = tanker / warrior / mage: '))
        if answer == "t": 
            return answer
        elif answer == "w":
            return answer
        elif answer == "m":
            return answer    
        else:
            print("input error try again!")
