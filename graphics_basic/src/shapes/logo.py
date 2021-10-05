import math

from shapes.fillPolygon import fill_polygon
from utils.getColor import get_color


def octagon_radius(_side):
    return _side * (math.sqrt(4 + 2 * math.sqrt(2)) / 2)


def octagon_angle():
    return 360 / 8


def octagon_side_angle():
    return (180 - octagon_angle()) / 2


def default(shape, _angle):
    shape.right(_angle)
    shape.hideturtle()
    shape.speed(0)


def octagon(_length, _side):
    for i in range(_length):
        angle = 360 / _length
        radius = octagon_radius(_side)
        fill_polygon(
            [
                [radius, octagon_side_angle()],
                [_side, octagon_side_angle()],
                [radius, octagon_angle()]
            ],
            get_color(i),
            lambda s: default(s, i * angle - 45 / 2)
        )
