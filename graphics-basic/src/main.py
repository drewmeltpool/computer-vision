import turtle;
from shapes.square import square
from shapes.circle import circle
from utils.shapeGroup import shapeGroup

window = turtle.Screen()

squareGroup = shapeGroup(square)
circleGroup = shapeGroup(circle)

squareGroup(
    [-200, 0],
    20,
    10,
    lambda s, i: -(s * i) / 2,
    lambda shape, offset, side, i, p:
        shape(side * i, p + offset[0], p + offset[1])
)

circleGroup(
    [200, 0],
    20,
    10,
    lambda s, i: -(s * i) / 2,
    lambda shape, offset, side, i, p:
        shape(side * i / 2, offset[0], (-side * i / 2) + offset[1])
)

window.mainloop()