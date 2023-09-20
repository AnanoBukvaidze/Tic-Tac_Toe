import random
#function that prints out a board (3 by 3)
def display_board(board):   
    print("\n" * 100)
    print(board[1] + "|" + board[2] + "|" + board[3])
    print('_____')
    print(board[4] + "|" + board[5] + "|" + board[6])
    print('_____')
    print(board[7] + "|" + board[8] + "|" + board[9])


#function that takes in a player input and assigns their marker as 'X' or 'O'
def player_input():        
    marker = 'A'
        
    while marker != "X" and marker != "O":
        marker = input("player1: choose X or O? ").upper()

    player1 = marker

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    
    return (player1,player2)
            
#function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board
def place_marker(board, marker, position):
    board[position] = marker

#checks the winner
def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (board[7] == board[8] == board[9] == mark) or (board[1] == board[4] == board[7] == mark) 
            or (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark) or (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark))

#function that randomly decides which player goes first
def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return "player 1"
    else:
        return "player 2" 

#function that returns boolean value if there is any freely available position on board
def space_check(board, position):
    for position in board:
        if position != "X" and position != "O":
            return True
        return False
        
#function that checks if the board is full
def full_board_check(board):
    x = 0
    for i in board:
        if i == "X" or i == "O":
            x += 1
            if x >= 10:
                return True
            else:
                return False
            
#function that asks for a player's next position and then uses the function from step 6 to check if it's a free position.
def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("choose a position: (1-9) "))
        return position
    

#function that asks the player if they want to play again and returns a boolean True if they do want to play again        
def replay():
    x = input("Do you want to continue playing? ").lower()

    if x == "yes":
        return x

print("Welcome to Tic Tac Toe!")

while True:
    # Set the game up here
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + "will go first")

    play_game = input("Ready to play? ").upper()
    if play_game == "YES":
        game_on = True
    else: game_on = False

    #while game_on:
    while game_on:
        
        #Player 1 Turn
        if turn == 'player 1':
            display_board(the_board)
            x = player_choice(the_board)
            place_marker(the_board, player1_marker, x)
            
            if win_check(the_board, player1_marker):
                print(the_board, "the winner - player 1")
                game_on = False
            
            else:
                if full_board_check(the_board) == True:
                    display_board(the_board)
                    print('tie!')
                    game_on = False
                else:
                    turn = 'player 2'

        
        # Player2's turn.
        else:
            display_board(the_board)
            y = player_choice(the_board)
            place_marker(the_board, player2_marker, y)

            if win_check(the_board, player2_marker):
                print(the_board, "the winner - player 2")
                game_on = False
            
            else:
                if full_board_check(the_board) == True:
                    display_board(the_board)
                    print('tie!')
                    game_on = False

                else:
                    turn = 'player 1'
            
    if not replay():
        break
        







            
    

