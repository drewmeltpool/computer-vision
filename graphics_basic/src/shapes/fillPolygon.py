from shapes.shape import shape
from shapes.polygon import polygon
from shapes.fill import fill


def fill_polygon(lines, color, cb):
    return fill(shape(), color, lambda s: polygon(s, lines, cb))
