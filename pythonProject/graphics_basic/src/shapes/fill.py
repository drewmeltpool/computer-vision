def fill(shape, color, cb):
    shape.color(color, color)
    shape.begin_fill()
    cb(shape)
    shape.end_fill()
    return shape