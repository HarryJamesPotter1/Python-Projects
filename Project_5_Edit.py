from typing import Tuple, Optional, Callable
from turtle import Turtle, Screen, mainloop, onscreenclick


Piece = Tuple[str, Callable[[],None]]
Board = Tuple[Tuple[Piece]]


ROWS = 3
COLS = 3
WIDTH = 600
HEIGHT = 600
TOP = HEIGHT // 2
BOTTOM = -TOP
RIGHT = WIDTH // 2
LEFT = -RIGHT
ROW_SIZE = HEIGHT // ROWS
COL_SIZE = WIDTH // COLS

turtle = Turtle()
screen = Screen()
screen.setup(WIDTH,HEIGHT)
screen.bgcolor('#3E033D')
turtle.penup()
turtle.hideturtle()
screen.tracer(0)
turtle.width(5)

CoordPair = Tuple[int, int]

def draw_line(start: CoordPair, end: CoordPair) -> None:
    """Draw line from start to end"""
    turtle.penup()
    turtle.goto(start)
    turtle.pen()
    turtle.goto(end)

EMPTY: Piece = ('',lambda : None)
X: Piece = ('X',draw_x)
O: Piece = ('O',draw_o)

def draw_grid() -> None:
    """Draws the tic tac toe board to screen"""
    for y in range(BOTTOM + ROW_SIZE, TOP, ROW_SIZE):
        draw_line((LEFT,y), (RIGHT,y))

    for x in range(LEFT + COL_SIZE, RIGHT, COL_SIZE):
        draw_line((x,TOP),(x,BOTTOM))

def show_board(board: Board) -> None:
    """Prints board to the screen"""
    draw_grid()
    for i, row in enumerate(board):
        y = TOP - (ROW_SIZE * i) - (ROW_SIZE / 2)
        for j, cell in enumerate(row):
            x = LEFT + (COL_SIZE * j) - (COL_SIZE / 2)
            turtle.penup()
            turtle.goto(x,y)
            cell[1]()            

    screen.update()

def row_count(board: Board) -> int:
    """Returns number of rows in board"""
    return len(board)

def col_count(board: Board) -> int:
    """Returns number of cols in board"""
    return len(board[0])

def can_play(board: Board, row: int, col: int) -> bool:
    """Checks if a piece can be played in a given position"""
    return board[row][col] == EMPTY

def full(board: Board) -> bool:
    """returns True when board is full, otherwise returns False"""
    for row in board:
        if EMPTY in row:
            return False
    
    return True

def check_x_in_a_row(vals, item) -> bool:
    """determines if a list contains three of the given items in a row"""

    if all(val == item for val in vals):
        return True

    return False

def win_in_row(board: Board, row: int, piece: Piece) -> bool:
    """Determine if a player has won given the row"""
    return check_x_in_a_row(board[row],piece)

def win_in_col(board: Board, col: int, piece: Piece) -> bool:
    """Determines whether a player has won in the given column"""
    
    selected_col = tuple(row[col] for row in board)
    return check_x_in_a_row(selected_col,piece)

def win_in_any_diag(board: Board, piece: Piece):
    """Determines whether a player has won in any diagonal"""
    indices = range(row_count(board))
    left_diag = tuple(board[i][i] for i in indices)
    right_diag = tuple(board[i][j] for i,j in zip(indices, indices[::-1]) )
 
    return check_x_in_a_row(left_diag, piece) or check_x_in_a_row(right_diag, piece)

def win_in_any_row(board: Board, piece: Piece):
    """Checks every row for a win"""
    return any(win_in_row(board, i, piece) for i in range(row_count(board)))

def win_in_any_col(board: Board, piece: Piece):
    """Checks every column for a win"""
    return any(win_in_col(board, i, piece) for i in range(col_count(board)))

def win(board: Board, piece: Piece):
    """Checks if the given piece has won"""

    return win_in_any_col(board, piece) or win_in_any_row(board, piece) or win_in_any_diag(board, piece)

def play(board: Board, row: int, col: int, piece: Piece) -> Board:
    """Updates the board with the given piece at the given location."""

    new = ()

    for i, old_row in enumerate(board):

        if i == row:
            updated = old_row[0:col] + (piece,) + old_row[col+1:]
            new += (updated,)
        
        else:
            new += (old_row,)

    return new

def get_player_input() -> Optional[Tuple[int,int]]:
    """Returns the grid coordinate of the player's choice, or -1 on quit"""

    while True:
        inp = input("Enter grid coordinate to play at (e.g 0,0 for the top left corner) or q to quit").lower()

        if inp == 'q':
            return -1

        else:
            vals = inp.split(',',maxsplit=1)
            all_numeric = all(val.strip().isnumeric() for val in vals)

            if all_numeric and len(vals) == 2:
                return int(vals[0]), int(vals[1])
        
            else:
                print('Invalid input, try again')

def handle_player_turn(board: Board, piece: Piece) -> Optional[Tuple[Board, bool]]:

    while True:
        player_input = get_player_input()

        if player_input is None:
            return

        row, col = player_input
        if can_play(board, row, col):
            board = play(board, row, col, piece)
            show_board(board)
            board_full = full(board)
            player_won = win(board,piece)
            if player_won:
                print(f'{piece} won!')
            elif board_full:
                print("Board full, it's a tie!")

            return board, (player_won or board_full)
        else:
            print('Invalid move')

if __name__ == "__main__":
    
    board: Board = ((EMPTY,) * COLS,) * ROWS
    players = (X,O)
    total_turns = 0

    show_board(board)

    while True:
        player = players[total_turns % len(players)]
        print(f'{player} is playing')
        result = handle_player_turn(board,player)

        if result is None:
            break
        total_turns += 1
        board, game_over = result

        if game_over == True:
            print('Game Over!')
            break