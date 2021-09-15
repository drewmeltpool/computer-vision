import turtle

def circle(radius, x = 0, y = 0):
    circle = turtle.Turtle()
    circle.hideturtle()
    circle.speed(0)
    circle.up()
    circle.setpos(x,y)
    circle.down()
    circle.circle(radius)