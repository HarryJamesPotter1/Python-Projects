from turtle import Turtle, mainloop

def tree(plist, length=200, angle=90, factor=0.63, width=20):
    # Angle: 45, 120, 90, 150, 230
    # Factor: 0.70
    # 65 A
    # 12 W
    """plist is list of pens
    length is length of branch
    angle is half of the angle between 2 branches
    factor is the factor by which branch is shortened
    from level to level.
    width is the width of the current level of branches"""
    if length > 3:
        lst = []
        # Draw two branches for each base branch (possibly just the trunk)
        for p in plist:
            p.width(width)
            if length < 7:
                p.color('lawngreen')

            p.forward(length)
            q = p.clone()
            p.left(angle)
            q.right(angle)
            lst.append(p)
            lst.append(q)
        # Draw two branches for each of the branches we just drew
        tree(lst, length * factor, angle, factor, width * 0.85)
        # print(len(lst))

if __name__ == "__main__":
    p = Turtle()
    p.speed(0)
    p.setundobuffer(None)
    p.hideturtle()
    # Speed up by uncommenting these
    # p.speed(0)
    # p.getscreen().tracer(30)
    p.left(90)
    p.penup()
    p.forward(-210)
    p.pendown()
    p.color('brown')
    tree([p])

    mainloop()
