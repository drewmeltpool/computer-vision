from graphics_basic.src.shapes.circle import circle
from graphics_basic.src.utils.shapeGroup import shape_group


def create_circle_group(_offset, size, amount):
    circle_shape_group = shape_group(circle)

    return circle_shape_group(
        _offset,
        size,
        amount,
        lambda s, i: -(s * i) / 2,
        lambda shape, offset, side, i, p:
            shape(side * i, offset[0], (-side * i) + offset[1])
    )
