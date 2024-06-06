import math
from vpoint import VPoint

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
POPULATION_SIZE = 1500
MAX_MOVES = 100
VELOCITY = 0.03
MUTATION_RATE = 0.1
RADIUS = 0.01

# Goal position
GOAL = VPoint(0.5, 0.1)

# Colors
RED = "#FF0000"
GREEN = "#00FF00"
BLUE = "#0000FF"
YELLOW = "#FFFF00"
WALL_COLOR = "#808080"

# Dot Types Colors
DOT_COLORS = {
    'red': RED,
    'green': GREEN,
    'blue': BLUE,
    'yellow': YELLOW,
    'wall': WALL_COLOR,
}

# Walls (defined as a list of tuples with start and end points)
WALLS = [
    (VPoint(0, 0), VPoint(1, 0)),
    (VPoint(1, 0), VPoint(1, 1)),
    (VPoint(1, 1), VPoint(0, 1)),
    (VPoint(0, 1), VPoint(0, 0)),
    
    (VPoint(0.3, 0.3), VPoint(0.7, 0.3)),
    (VPoint(0.7, 0.3), VPoint(0.3, 0)),
    (VPoint(1, 0.7), VPoint(0.7, 0)),
    # (VPoint(0.3, 0.7), VPoint(0.3, 0.3))
]
