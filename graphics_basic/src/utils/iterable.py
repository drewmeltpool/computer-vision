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


def foreach(arr, cb):
    for i in range(len(arr)):
        cb(arr[i], i)


def map(arr, _cb):
    array = []
    foreach(
        arr,
        lambda item, i: array.append(_cb(item, i))
    )

    return array

