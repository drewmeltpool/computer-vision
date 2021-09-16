import turtle;
from utils.iterable import range_foreach

def square(side, x = 0, y = 0):
    _square = turtle.Turtle()
    _square.speed(0)
    _square.hideturtle()
    _square.up()
    _square.setpos(x, y)
    _square.down()
    range_foreach(
        4,
        lambda _x,_y: (
            _square.forward(side),
            _square.left(90)
        )
    )
