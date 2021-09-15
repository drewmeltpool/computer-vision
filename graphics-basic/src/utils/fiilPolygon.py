from utils.shape import shape
from utils.polygon import polygon
from utils.fill import fill

def fillPolygon(lines, color, cb):
    return fill(shape(), color, lambda s: polygon(s, lines, cb))
