import func_script
import character 
unit = []
rounds = 1
player_units = []
ai_units = []


def main():
    exit = "x"
    end = ""
    
    while exit != end:
        #select_player_units()
        num_unit = int(input("select number of units: "))
        player_units = func_script.setup_player(num_unit)
        ai_units = func_script.setup_ai(len(player_units))
        '''
        
        setup_ai_units()
        player_attack_ai_unit() / ai_attack_player()
        check player or ai win
        print event logs

        
        '''
        for i in range(len(player_units)):
            print(player_units[i].__str__())
        print("\n")
        for i in range(len(player_units)):
            print(ai_units[i].__str__())    
        end = str(input("x to end"))   
main()