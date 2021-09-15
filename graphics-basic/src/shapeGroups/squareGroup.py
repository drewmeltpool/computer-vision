from shapes.square import square
from utils.shapeGroup import shapeGroup

def createSquareGroup(offset, size, amount):
    squareShapeGroup = shapeGroup(square)

    return squareShapeGroup(
        offset,
        size,
        amount,
        lambda s, i: -(s * i) / 2,
        lambda shape, offset, side, i, p:
            shape(side * i, p + offset[0], p + offset[1])
    )