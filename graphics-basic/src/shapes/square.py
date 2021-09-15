import turtle;

def square(side, x = 0, y = 0):
    square = turtle.Turtle()
    square.speed(0)
    square.hideturtle()
    square.up()
    square.setpos(x, y)
    square.down()
    for i in range(4):
        square.forward(side)
        square.left(90)
