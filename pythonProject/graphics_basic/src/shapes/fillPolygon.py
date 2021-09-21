from graphics_basic.src.shapes.shape import shape
from graphics_basic.src.shapes.polygon import polygon
from graphics_basic.src.shapes.fill import fill


def fill_polygon(lines, color, cb):
    return fill(shape(), color, lambda s: polygon(s, lines, cb))
