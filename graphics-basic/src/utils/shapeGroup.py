def shape_group(shape):
    def shape_group_inner(offset, side, amount, pos, handle_shape):
        for i in range(amount):
            handle_shape(shape, offset, side, i, pos(side, i))
    return shape_group_inner