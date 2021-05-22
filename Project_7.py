from turtle import Turtle, Screen, done
from time import sleep


WIDTH = 600
HEIGHT = 600

colours = ['red', 'darkorange', 'yellow', 'lime', 'cyan', 'black', 'gold', 'fuchsia', 'saddlebrown']
clicks = 0
colour = colours[clicks]

turtle = Turtle(shape='square')
turtle.speed(0)
turtle.color(colour)
turtle.shapesize(1.5,1.5,2)

screen = Screen()
screen.setup(WIDTH,HEIGHT)
#Ensures turtle is dragged smoothly on the screen
screen.delay(0)

colour_box_size = 3
colour_box = Turtle(shape='square')
colour_box.fillcolor(colour)
colour_box.shapesize(colour_box_size,colour_box_size,2)
colour_box.pu()

colour_box.goto(WIDTH / 2 - 40, HEIGHT / 2 - 30)

def switch_color(_, __):
    global clicks
    clicks += 1
    colour = colours[clicks % len(colours)]
    turtle.color(colour)
    colour_box.fillcolor(colour)

turtle.ondrag(turtle.goto)
screen.onclick(switch_color,3)
colour_box.onclick(switch_color)

width_keys = ['0','1','2','3','4','5','6']

def set_width_from_key(key):
    turtle.width(int(key) * 10 + 5)

def get_width_key_handler(width_key):
    def handler():
        set_width_from_key(width_key)
    return handler

for width_key in width_keys:
    width_key_handler = get_width_key_handler(width_key)
    screen.onkey(width_key_handler,width_key)

set_width_from_key(width_keys[0])

def toggle_draw():
    if turtle.isdown():
        turtle.penup()
    else:
        turtle.pendown()

screen.onkey(toggle_draw, 'space')
screen.listen()
done()