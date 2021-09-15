from shapes.circle import circle
from utils.shapeGroup import shapeGroup

def createCircleGroup(offset, size, amount):
    circleShapeGroup = shapeGroup(circle)

    return circleShapeGroup(
        offset,
        size,
        amount,
        lambda s, i: -(s * i) / 2,
        lambda shape, offset, side, i, p:
        shape(side * i, offset[0], (-side * i) + offset[1])
    )