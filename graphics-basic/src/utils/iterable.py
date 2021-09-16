def range_foreach(len, _cb):
    for _i in range(len):
        _cb(_i, range)

def range_map(len, _cb):
    array = []
    range_foreach(
        len,
        lambda i, range: array.append(_cb(i, range))
    )

    return array