def shapeGroup(shape):
    def shapeGroupInner(offset, side, amout, pos, handleShape):
        for i in range(amout):
            p = pos(side, i)
            handleShape(shape, offset, side, i, p)
    return shapeGroupInner