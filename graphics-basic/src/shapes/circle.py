import turtle

def circle(radius, x = 0, y = 0):
    _circle = turtle.Turtle()
    _circle.hideturtle()
    _circle.speed(0)
    _circle.up()
    _circle.setpos(x,y)
    _circle.down()
    _circle.circle(radius)