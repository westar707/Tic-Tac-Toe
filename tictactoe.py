#----Global Varieables----

#Game board
board = ["-", "-", "-", "-", "-", "-",  "-", "-", "-"]

# If game is still going
game_still_going = True

# who one? or tie?
winner = None

# Whos turn is it?
current_player = "X"


# Play a game of tic tac toe
def play_game():
    
    # Display initial board
    display_board()

    #while the game is still going
    while game_still_going:
        
        # handle a single turn of an arbitrary player
        handle_turn(current_player)
        
        # check if game has ended
        check_if_game_over()

        #flip to the other player
        flip_player()

# The game has ended
if winner == "X" or winner == "O":
    print(winner + "Won.")
elif winner == None:
    print("Tie.")

    # Display Board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


#handel a single turn of an arbitary player
def handle_turn(player):
    print(player + 's turn.')
    position = input("Choose a position from 1-9: ")
    position = int(position) 

    #whatver the user input, make sure it is vaid and spot is open
    valid = False
    while not valid:
        #make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input ("Choose a Position fron 1-9")

        # get correct index in our board list
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

        #Put the game piece on the board
        board[position] = player
        
        #show the game board
        display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    #set up global variables
    global winner


    #check rows
    row_winner = check_rows()
    #check colums
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        #there was a win
        winner = row_winner()
    elif column_winner:
        #there was a win
        winner = column_winner()
    elif diagonal_winner:
        #there was a win
        winner = diagonal_winner()
    else:
        #there was no win
        winner = None 
        return

def check_rows():
    #set up global variables
    global game_still_going
    #check if any of the rows all have the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #if ant row does have a match flag, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None

def check_columns():
    #set up global variables
    global game_still_going
    #check if any of the rows all have the same value (and is not empty)
    column_1 = board[0] == board[1] == board[2] != "-"
    column_2 = board[3] == board[4] == board[5] != "-"
    column_3 = board[6] == board[7] == board[8] != "-"
    #if ant row does have a match flag, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else: 
        return None 

def check_diagonals():
    #set up global variables
    global game_still_going
    #check if any of the rows all have the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    #if any row does have a match flag, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # return the winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    else:
        return None

#check for tie 
def check_if_tie():
    #Set global variables
    global game_still_going
    #if board is full
    if "-" not in board:
        game_still_going = False
        return True
    #else there is no tie
    else:
        return False

def flip_player():
    #global variable we need
    global current_player
    #if the current play was x make it o
    if current_player == "X":
        current_player = "O"
    #or if the current player owas O make it X
    elif current_player == "O":
        current_player = "X"

#-------- Start Execution------
#Play a Game of Tic Tac Toe ------

play_game()

