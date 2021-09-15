import turtle;

def square(side, x = 0, y = 0):
    _square = turtle.Turtle()
    _square.speed(0)
    _square.hideturtle()
    _square.up()
    _square.setpos(x, y)
    _square.down()
    for _ in range(4):
        _square.forward(side)
        _square.left(90)
