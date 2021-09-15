import turtle, math

from shapeGroups.squareGroup import create_square_group
from shapeGroups.circleGroup import create_circle_group
from shapes.fiilPolygon import fill_polygon
from utils.getColor import get_color

window = turtle.Screen()

# 1 Task

create_square_group([-200, 0], 50, 5)
create_circle_group([200, 0], 25, 5)

# 2 Task

def range_map(range, cb):
    array = []
    for _i in range:
        array.append(cb(arr[_i], _i, range))

    return array



def octagon_radius (_side):
    return _side * (math.sqrt(4 + 2 * math.sqrt(2)) / 2)

def octagon_angle():
    return 360 / 8

def octagon_side_angle():
    return (180 - octagon_angle()) / 2


def default(shape, _angle):
    shape.right(_angle)
    shape.hideturtle()
    shape.speed(0)

length = 4
side = 200

for i in range(length):
    angle = 360 / length
    radius = octagon_radius(side)
    fill_polygon(
        [
            [radius, octagon_side_angle()],
            [side, octagon_side_angle()],
            [radius, octagon_angle()]
        ],
        get_color(i, length),
        lambda s: default(s, i * angle - 45 / 2)
    )

window.mainloop()