import turtle

Turtle = turtle

Turtle.color("Brown")
Turtle.left(90)
Turtle.speed(0)
def Tree(length, width):
    # Tree is a function that recursively makes a tree of stem-length length# your own code
    Turtle.width(width)
    if length <= 5:
        # Base Case# your own code
        Turtle.color("Lawngreen")
        Turtle.forward(length)
        Turtle.left(30)
        Turtle.forward(0.75*length)
        Turtle.backward(0.75*length)
        Turtle.right(60)
        Turtle.forward(0.75*length)
        Turtle.backward(0.75*length)
        Turtle.left(30)
        Turtle.backward(length)
        Turtle.color("Brown")
    else:
        # Recursive Case# your own code
        Turtle.forward(length)
        Turtle.left(30)
        Tree(0.75*length, 0.8*width)
        Turtle.right(60)
        Tree(0.75*length, 0.8*width)
        Turtle.left(30)
        Turtle.backward(length)
Tree(30, 10)
