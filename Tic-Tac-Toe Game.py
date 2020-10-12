#  creating some Global variables
board = [' ']*10
game_state = True
announce = ''

# functin that reset the board
# note: game will ignore 0 index

def reset_board():
    global board,game_state
    board = [' ']*10
    game_state = True

# function to display the board
def display_board():
    print('\n'*100)        #clear the output
    print('     |      |')
    print(' '   +board[7]+ '   |  '+ board[8]+ '   |  '+ board[9])
    print('     |      |')
    print('------------------')
    print('     |      |')
    print(' '   +board[4]+ '   |   '+ board[5]+ '  |   '+ board[6])
    print('     |      |')
    print('------------------')
    print('     |      |')
    print(' '   +board[1]+ '   |   '+ board[2]+ '  |   '+ board[3])
    print('     |      |')
        

# function for checkinf for win 
def win_check(board,player):
    
    if (board[7]== board[8]== board[9] == player) or \
        (board[4]== board[5]== board[6] == player) or \
        (board[1]== board[2]== board[3] == player) or \
        (board[7]== board[4]== board[1] == player) or \
        (board[8]== board[5]== board[2] == player) or \
        (board[9]== board[6]== board[3] == player) or \
        (board[9]== board[5]== board[1] == player) or \
        (board[7]== board[5]== board[3] == player):
        return True
    
    else:
        return False
    
    
# full board check in case of tie 
def full_board_check(board): 
    if " " in board[1:]:
        return False
    else:
        return True
        


# asks the player where to place the marker
def ask_player(mark):
    
    global board
    request = "choose where to place mark: " + mark +"\n"
    
    while True:
        try:
            choice = int(input(request))
        except ValueError:
            print('Sorry! please enter between 1-9')
            continue
            
        if board[choice] == " ":
            board[choice] = mark
            break
            
            
        else:
            print('oops!! empty space detected')
            continue




def player_choice(mark):
    global board,game_state,announce
    
    announce= " "          #set the blank game announcement
    mark = str(mark)       #get inpit from player
    ask_player(mark)       #validate the input
    
    # check for win
    if win_check(board,mark):
        print('\n'*100)
        display_board()
        announce = mark +  "\nYOU WIN!!"
        game_state = False
        
    print('\n'*100)
    display_board()    
    
    # check for Tie 
    if full_board_check(board):
        announce = "Tie!!"
        game_state = False
        
    return game_state, announce    



def play_game():
    reset_board()
    global announce
     
    #  set mark 
    X = 'X'.upper()
    O = 'O'.upper()
    
    while True:
        print('\n'*100)
        display_board()
        
        # player X turn 
        game_state,announce = player_choice(X)
        print(announce)
        if game_state == False:
            break
             
        #  player Y turn     
        game_state,announce = player_choice(O)
        print(announce)
        if game_state == False:
            break

    #  asks for rematch        
    rematch = input(' press y to play again or hit any key to Quit ')
    
    if rematch == 'y':
        play_game()
    else:
        print("Thanks For Playing")
            
play_game()                                