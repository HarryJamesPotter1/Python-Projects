from typing import Tuple, Optional, Callable
from turtle import Turtle, Screen, mainloop, onscreenclick
import math
import time


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
screen.bgcolor('#a6e6ff')
turtle.penup()
turtle.hideturtle()
screen.tracer(0)
turtle.width(5)


CoordPair = Tuple[int, int]

def draw_line(start: CoordPair, end: CoordPair) -> None:
    """Draw line from start to end"""
    turtle.penup()
    turtle.goto(start)
    turtle.pendown()
    turtle.goto(end)

def draw_o() -> None:
    radius = COL_SIZE / 3
    x, y = turtle.position()
    turtle.penup()
    turtle.goto(x,y - radius)
    turtle.pendown()
    turtle.circle(radius)

def draw_x() -> None:
    x, y = turtle.position()
    half_width = COL_SIZE / 4
    half_height = ROW_SIZE / 4
    left = x - half_width;
    right = x + half_width
    bottom = y - half_height
    top = y + half_height
    draw_line((left, top),(right, bottom))
    draw_line((right, top), (left, bottom))

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
    turtle.clear()
    draw_grid()
    for i, row in enumerate(board):
        y = TOP - (ROW_SIZE * i) - (ROW_SIZE / 2)
        for j, cell in enumerate(row):
            x = LEFT + (COL_SIZE * j) + (COL_SIZE / 2)
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

def handle_player_turn(board: Board, piece: Piece, coords: CoordPair) -> Optional[Tuple[Board,bool,bool]]:
    """ Handles the player's turn and returns the result.
    
    :return: `(board, game_over, valid)` where board is the updated board
    game over indicates if the game is finished after the user's turns,
    valid indicates if the move was valid
    
    """

    row, col = coords
    if can_play(board, row, col):
        board = play(board, row, col, piece)
        show_board(board)
        board_full = full(board)
        player_won = win(board,piece)
        if player_won:
            write_message(f'{piece[0]} won!')
        elif board_full:
            write_message("Board full, it's a tie!")

        return board, (player_won or board_full), True
    else:
        print('Invalid move')
        return board, False, False

def write_message(message: str, top_offset=50) -> None:
    """Takes a message and writes it to the turtle scren
    param: top_offset: adjusts the height of the text from the middle"""

    turtle.goto(0,HEIGHT / 2 - top_offset) 
    turtle.write(message, align="center", font=('Arial',30,'normal'))

def coords_from_click(x: float, y: float) -> CoordPair:
    percent_from_top = (TOP - y)/ HEIGHT
    row = math.floor(ROWS * percent_from_top)
    percent_from_left = (RIGHT + x) / WIDTH
    col = math.floor(COLS * percent_from_left)
    return row, col

board = ((EMPTY,) * COLS,) * ROWS
players = (X,O)
total_turns = 0

def handle_click(x,y):
    global board
    global total_turns
    player = players[total_turns % len(players)]
    print(f'{player[0]} is playing')
    coords = coords_from_click(x, y)
    board, game_over, valid = handle_player_turn(board, player, coords)
    if valid:
        total_turns += 1
        if game_over:
            write_message('Game over!', top_offset =150)
            onscreenclick(None)
    else:
        write_message("Invalid Move")

if __name__ == "__main__":

    show_board(board)
    onscreenclick(handle_click)
    mainloop()