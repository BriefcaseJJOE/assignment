import func_script as fuc
import character 
import random


rounds = 1
player_units = []
ai_units = []



def main():
    
    exit = "x"
    end = ""
    ai_life = 0
    player_life = 0
    player_unit = 0
    ai_unit = 0
    
    while exit != end:
        global rounds
        
        #setting up player units in a list
        num_unit = int(input("select number of units: "))
        player_units = fuc.setup_player(num_unit)

        
        # setting up ai units in a list
        ai_units = fuc.setup_ai(len(player_units))


        # update life on how many units player and ai have number of unit = number of life
        player_life = len(player_units)
        ai_life = len(ai_units)

        #
        player_unit_to_atk = 0
        ai_unit_to_atk = 0

        # keeping track of player unit hp and ai unit hp
        php = player_units[player_unit].hp
        ahp = ai_units[ai_unit].hp

        #end loop when player or ai run out of units / life
        while ai_life >= 1:
 
            fuc.clear_screen()
            


            #setting up turn base attack player go first
            if rounds % 2 == 1 :
                #show selected units and ai units 
                fuc.show_game_board(player_units,ai_units)
            
                #@@@@@@player can select a unit to atk the other unit@@@@@

                #player select which of their own unit to attack
                player_unit_to_atk = int(input("select unit to attack (1 for 1st unit, 2 for 2nd unit etc...: ") )
                player_unit_to_atk -= 1
                #catch out of range input default to first unit
                if player_unit_to_atk < 0 or player_unit_to_atk > len(player_units):
                    player_unit_to_atk = 0
                
                
                #player select which ai unit to attack
                ai_unit_to_atk = int(input("select ai_unit to attack (1 for 1st unit, 2 for 2nd unit etc...: "))
                ai_unit_to_atk -= 1
                if ai_unit_to_atk < 0 or ai_unit_to_atk > len(ai_units):
                #catch out of range input and default to first unit
                    ai_unit_to_atk = 0

                fuc.clear_screen()
                
                #process atk calculation
                player_units[player_unit_to_atk].attack(ai_units[ai_unit_to_atk])
                fuc.show_game_board(player_units,ai_units)
            else:
                ai_units[random.randint(0,len(ai_units)-1)].attack(player_units[random.randint(0,len(ai_units)-1)])  
                fuc.show_game_board(player_units,ai_units)  

            
            #show state of player and ai unit    
            #show game state
           
            
            #update hp state
            php = player_units[player_unit].hp
            ahp = ai_units[ai_unit].hp
            
            #if player unit die update life of player 
            #and activate next unit 
            # if php <= 0:
                # player_life -= 1
                # player_unit += 1
            # elif ahp <= 0:
                # ai_life -= 1
                # ai_unit += 1


            
            #print(ai_life)
            #print(player_life)
            #print(ahp,php)
            #print(rounds)
            rounds += 1
            p = str(input("press enter to continue:"))
            
        '''
        update game state
        
        
        check player or ai win
        print event logs

        
        '''
        
        
        end = str(input("x to end"))   
main()
