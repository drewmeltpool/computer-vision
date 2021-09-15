import turtle, math

from shapeGroups.squareGroup import createSquareGroup
from shapeGroups.circleGroup import createCircleGroup
from utils.fiilPolygon import fillPolygon
from utils.randomColor import colors


window = turtle.Screen()

# 1 Task

# createSquareGroup([-200, 0], 50, 5)
# createCircleGroup([200, 0], 25, 5)

# 2 Task

def rangeMap(range, cb):
    array = []
    for i in range:
        array.append(cb(arr[i], i, range))

    return array

def octagonRadius (side):
    return side * (math.sqrt(4 + 2 * math.sqrt(2)) / 2)

def octagonAngle():
    return 360 / 8

def octagonSideAngle():
    return (180 - octagonAngle()) / 2

lenght = 4
side = 200

def default(shape, angle):
    shape.right(angle)
    shape.hideturtle()
    shape.speed(0)

for i in range(lenght):
    angle = 360 / lenght
    radius = octagonRadius(side)
    fillPolygon(
        [
            [radius, octagonSideAngle()],
            [side, octagonSideAngle()],
            [radius, octagonAngle()]
        ],
        colors(i, lenght),
        lambda s: default(s, i * angle - 45 / 2)
    )

window.mainloop()