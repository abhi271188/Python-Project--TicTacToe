# ------------ Design of the game board ----------------------------------------
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
# ------------------------------------------------------------------------------
active_player = 'X'                                     # first turn of the game
game_is_still_active = True                             # Initially the game is active
winner = None

# ------------ A driver function that displays the game board-------------------
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
# ------------------------------------------------------------------------------
# ----------- A driver function that drives the whole game ---------------------
def play_game():
    global game_is_still_active
    display_board()
    while(game_is_still_active):
        handle_turns(active_player)
        game_is_ended_or_not()

# ------------------------------------------------------------------------------
# ----------- A driver function that manages the turns of both players ---------
def handle_turns(curr_player):
    position = int(input('Enter the position from 1 to 9: '))
    position = position - 1
    board[position] = curr_player
    display_board()
# -------------------------------------------------------------------------------
# ----------- A driver function that checks whether the game is over or not -----
def game_is_ended_or_not():
    check_for_win()
    #check_for_tie()
# -------------------------------------------------------------------------------
# ----------- A driver function that gives us the winner of the game ------------
def check_for_win():
    global active_player
    row_win = check_row_win()
    #check_col_win()
    #check_diag_win()
    if row_win:
        winner = row_win
# --------------------------------------------------------------------------------
# ----------- A driver function that checks the pattern in the rows --------------
def check_row_win():
    global game_is_still_active
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    if row_1 or row_2 or row_3:
        game_is_still_active = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    else:
        return board[6]
# ------------------------------------------------------------------------------------

play_game()