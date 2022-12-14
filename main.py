
import func_script as fuc
import character 
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


rounds = 1
player_units = []
ai_units = []
player_coins = 0
ai_coins = 0

def main():
    
    exit = "x"
    end = ""
   
    
    while exit != end:
        # global ai_coins
        # global player_coins
        global rounds
        
        logger.info('new game started.')

        #setting up player units in a list
        num_unit = fuc.unit_checker()
        player_units = fuc.setup_player(num_unit)

        
        # setting up ai units in a list
        ai_units = fuc.setup_ai(len(player_units))


       
        player_unit_to_atk = 0
        ai_unit_to_atk = 0

       

        #end loop when player or ai run out of units / life
        while True:
            player_coins = 0
            ai_coins = 0 
            
            fuc.clear_screen()
            if ai_coins > 199:
                fuc.setup_ai(1)

            
            #setting up turn base attack player go first
            if rounds % 2 == 1 :
                
                
                #show selected units and ai units 
                fuc.show_game_board(player_units,ai_units)
                #@@@@@@player can select a unit to atk the other unit@@@@@

                #player select which of their own unit to attack
                player_unit_to_atk = fuc.input_checker_int_select()
                #correct from 1 indexing to 0 indexing
                player_unit_to_atk -= 1
                #catch out of range input default to first unit
                if player_unit_to_atk < 0 or player_unit_to_atk >= len(player_units):
                    player_unit_to_atk = 0
                
                
                #player select which ai unit to attack
                ai_unit_to_atk = fuc.input_checker_int_atk()
                #correct from 1 indexing to 0 indexing
                ai_unit_to_atk -= 1
                if ai_unit_to_atk < 0 or ai_unit_to_atk >= len(ai_units):
                #catch out of range input and default to first unit
                    ai_unit_to_atk = 0

                fuc.clear_screen()
                
                #process atk calculation
                player_units[player_unit_to_atk].attack(ai_units[ai_unit_to_atk])
                fuc.show_game_board(player_units,ai_units)
                
            

            else:
                
                ai_units[fuc.get_high_atk_unit(ai_units)].attack(player_units[fuc.get_high_atk_unit(player_units)]) 
                fuc.show_game_board(player_units,ai_units)  
                

                
           

        #if player unit or ai die remove unit from list 
                
            if fuc.check_hp_is_zero(player_units) == True:
                dead_unit = fuc.dead_unit_index(player_units)
                player_units.pop(dead_unit)            


            elif fuc.check_hp_is_zero(ai_units) == True:
                dead_unit = fuc.dead_unit_index(ai_units)
                ai_units.pop(dead_unit)

             #check if ai win
            if len(player_units)<= 0:
                print("Ai WIN")
                break   
            
            #check if player win
            if len(ai_units)<= 0:
                print("player WIN")
                break   


            
            rounds += 1
            dialog = str(input("press any key to continue:")).lower()
            
        
        
        rounds = 1
        end = str(input("x to end or any other key to play again:")).lower() 

if __name__ == '__main__':
    main()
