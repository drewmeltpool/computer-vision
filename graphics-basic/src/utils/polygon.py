def polygon(shape, lines, cb):
    cb(shape)
    for line in lines:
        shape.forward(line[0])
        shape.right(180 - line[1])
    return shape
