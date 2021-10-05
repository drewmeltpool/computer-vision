from shapes.square import square
from utils.shapeGroup import shape_group


def create_square_group(_offset, _size, _amount):
    square_shape_group = shape_group(square)

    return square_shape_group(
        _offset,
        _size,
        _amount,
        lambda s, i: -(s * i) / 2,
        lambda shape, offset, side, i, p:
        shape(side * i, p + offset[0], p + offset[1])
    )
