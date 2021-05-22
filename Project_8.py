from turtle import Turtle, Screen, done

ROWS = 8
COLS = 8
WIDTH = 800
HEIGHT = 800
TOP = HEIGHT // 2
BOTTOM = -TOP
RIGHT = WIDTH // 2
LEFT = -RIGHT
ROW_SIZE = HEIGHT // ROWS
COL_SIZE = WIDTH // COLS
DOT_SIZE = ROW_SIZE - 10

turtle = Turtle()
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
turtle.hideturtle()
screen.tracer(False)
turtle.speed(0)

turns = {'red': 'yellow', 'yellow': 'red'}
state = {'player': 'yellow', 'rows': [0] * 8}


def board():
    """draws the connect 4 board"""
    screen.bgcolor('cyan')

    #Column seperators
    for x in range(LEFT + COL_SIZE, RIGHT, COL_SIZE):
        turtle.penup()
        turtle.goto(x, TOP)
        turtle.pendown()
        turtle.goto(x, BOTTOM)

    #Dots centered within each column
    for x in range(LEFT + COL_SIZE // 2, RIGHT, COL_SIZE):
        for y in range(BOTTOM + ROW_SIZE // 2, TOP, ROW_SIZE):
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            turtle.dot(DOT_SIZE, 'white')

    screen.update()


def click(x: float, _):
    player = state['player']
    rows = state['rows']
    col = int((x + RIGHT) // COL_SIZE)
    row = rows[col]
    x =(col * COL_SIZE) - RIGHT + (COL_SIZE / 2)
    y = (row * ROW_SIZE) - TOP + (ROW_SIZE / 2)
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(DOT_SIZE, player)
    screen.update()
    rows[col] += 1
    state['player'] = turns[player]

board()
screen.onscreenclick(click)
done()