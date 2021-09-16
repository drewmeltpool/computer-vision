import turtle, math

from shapeGroups.squareGroup import create_square_group
from shapeGroups.circleGroup import create_circle_group
from shapes.logo import octagon
from utils.getColor import get_color

window = turtle.Screen()

# 1 Task

# create_square_group([-200, 0], 50, 5)
# create_circle_group([200, 0], 25, 5)

# 2 Task

octagon(4, 250)

window.mainloop()