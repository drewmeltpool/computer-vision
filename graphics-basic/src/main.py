import turtle
import math
from shapes.square import square
from shapes.circle import circle
from utils.shapeGroup import shapeGroup

window = turtle.Screen()

squareGroup = shapeGroup(square)
circleGroup = shapeGroup(circle)

squareGroup(
    [-200, 0],
    50,
    5,
    lambda s, i: -(s * i) / 2,
    lambda shape, offset, side, i, p:
        shape(side * i, p + offset[0], p + offset[1])
)

circleGroup(
    [200, 0],
    25,
    5,
    lambda s, i: -(s * i) / 2,
    lambda shape, offset, side, i, p:
        shape(side * i, offset[0], (-side * i) + offset[1])
)

# def createShape():
#     return turtle.Turtle()
#
# def createPolygon(shape, lines, cb):
#     cb(shape)
#     for line in lines:
#         shape.forward(line[0])
#         shape.right(line[1])
#     return shape
#
# def fill(shape, color, cb):
#     shape.color(color, color)
#     shape.begin_fill()
#     cb(shape)
#     shape.end_fill()
#     return shape
#
# def polygon(lines, color, cb):
#     return fill(createShape(), color, lambda s: createPolygon(s, lines, cb))
#
#
# side = 200
# radius = side * (math.sqrt(4 + 2 * math.sqrt(2)) / 2)
#
# def rotate(shape, angle):
#     shape.right(angle)
#
# polygon([[radius, 112.5], [side, 112.5], [radius, 135]], 'red', lambda s: rotate(s, 0))
# polygon([[radius, 112.5], [side, 112.5], [radius, 135]], 'green', lambda s: rotate(s, 90))
# polygon([[radius, 112.5], [side, 112.5], [radius, 135]], 'blue', lambda s: rotate(s, 180))
# polygon([[radius, 112.5], [side, 112.5], [radius, 135]], 'cyan', lambda s: rotate(s, 270))

window.mainloop()