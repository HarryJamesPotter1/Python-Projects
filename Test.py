from Project_5 import (
    EMPTY,
    O,
    X,
    can_play,
    check_x_in_a_row,
    col_count,
    full,
    play,
    row_count,
    show_board,
    get_player_input,
    win,
    win_in_any_col,
    win_in_any_diag,
    win_in_any_row,
    win_in_col,
    win_in_row
)

board = ((EMPTY,X,EMPTY), (O,X,O),(X,O,X))

print("Show board")
show_board(board)

#print("Now let us get the player input")
#player_input = get_player_input()
#print()
#print(player_input)

rows = row_count(board)

cols = col_count(board)

print("row:",rows)
print("cols:",cols)

#is_play = can_play(board,0,1)

print(play)

print("test play function")

board = ((EMPTY, X, EMPTY), (O, EMPTY, O), (X, O, EMPTY))

new_board = play(board, 0, 0, X)

print(new_board)

print("check x in a row function test")
print(check_x_in_a_row([1, 1, 1], 1))
print("check win in row function")
print(win_in_row(board, 1, X) == False)

row_win_board = ((O, O, O), (X, X, X), (EMPTY, EMPTY, EMPTY))
col_win_board = ((O, X, EMPTY), (O, X, EMPTY), (O, X, EMPTY))

print("win in any row or col")

print(win_in_any_row(row_win_board,X) == True)
print(win_in_any_row(row_win_board,O) == True)
print(win_in_any_col(col_win_board,X) == True)
print(win_in_any_col(col_win_board,O) == True)

print("win in any diag")

diag_win_board = ((O, X, EMPTY), (O, O, EMPTY), (O, X, O))

print(win_in_any_diag(diag_win_board,O) == True)
print(win_in_any_diag(diag_win_board,X) == False)

print("check if win function works")
print(win(row_win_board,X) == True)
print(win(col_win_board,O) == True)
print(win(diag_win_board, O) == True)

