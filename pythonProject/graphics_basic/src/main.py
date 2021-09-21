import turtle

import matplotlib.pyplot as plt
import numpy as np

from shapeGroups.squareGroup import create_square_group
from shapeGroups.circleGroup import create_circle_group
from shapes.logo import octagon
from utils.getColor import get_color
from utils.iterable import map 

window = turtle.Screen()

# 1 Task
create_square_group([-200, 0], 50, 5)
create_circle_group([200, 0], 25, 5)

# 2 Task
octagon(4, 250)

window.mainloop()


# 3 Task

def create_plot():
    return plt


def add_plot(_plot, val):
    _plot.plot(val[0], val[1])


def abscissa(min, max, range):
    return np.linspace(min, max, range)


def ordinate(arr, cb):
    return map(arr, lambda item, i: cb(item))


x = abscissa(0, 100, 10000)
y = lambda cb: ordinate(x, cb)

plot = create_plot()

# Закон І. – y(x) = (a * 0.01) * sin(x)
add_plot(plot, [x, y(lambda i: 3 * 0.01 * np.sin(i))])

# Закон ІІ. – y(x) = ((a + 3) * 0.01) * sin(x)
add_plot(plot, [x, y(lambda i: 6 * 0.01 * np.sin(i))])

# Закон ІІІ. – y(x) = (a * 0.01) * cos(x)
add_plot(plot, [x, y(lambda i: 3 * 0.01 * np.cos(i))])

plot.show()
