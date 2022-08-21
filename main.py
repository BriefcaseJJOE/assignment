import func_script as fuc
import character 

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


        #setting up ai units in a list
        ai_units = fuc.setup_ai(len(player_units))


        #update life on how many units player and ai have number of unit = number of life
        player_life = len(player_units)
        ai_life = len(ai_units)
            
        #keeping track of player unit hp and ai unit hp
        php = player_units[player_unit].hp
        ahp = ai_units[ai_unit].hp

        #end loop when player or ai run out of units / life
        while ai_life >= 1:
 
            

            fuc.clear_screen()

            #setting up turn base attack player go first
            if rounds % 2 == 1 :
                player_units[player_unit].attack(ai_units[ai_unit])
            else:
                ai_units[ai_unit].attack(player_units[player_unit])    

            #show state of player and ai unit    
            #player_attack_ai_unit() / ai_attack_player()
            fuc.update_player_units(len(player_units),player_units)
            print("\n")
            fuc.update_ai_units(len(ai_units),ai_units)
            
            #update hp state
            php = player_units[player_unit].hp
            ahp = ai_units[ai_unit].hp
            
            #if player unit die update life of player 
            #and activate next unit 
            if php <= 0:
                player_life -= 1
                player_unit += 1
            elif ahp <= 0:
                ai_life -= 1
                ai_unit += 1


            
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
