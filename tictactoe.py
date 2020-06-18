#----Global Varieables----

#Game board
board = ["-", "-", "-", "-", "-", "-",  "-", "-", "-"]

# If game is still going
game_still_going = True

# who one? or tie?

winner = None

# Whos turn is it?
current_player = "X"


# Display Board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

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

#handel a single turn of an arbitary player
def handle_turn(player):
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1

    board[position] = "X"

    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    #check rows
    row_winner = check_rows()
    #check colums
    column_winnwe = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()
    return 

def check_rows():
    return

def check_columns():
    return

def check_diagonals():
    return

def check_if_tie():
    return

def flip_player():
    return

play_game()
