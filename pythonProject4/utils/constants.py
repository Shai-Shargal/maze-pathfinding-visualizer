# utils/constants.py

MAZE_SIZE = 70
CELL_SIZE = 10

# Cell types
WALL = 1
SPACE = 0
START = 2
TARGET = 3
BLACK = 4
GRAY = 5
PATH = 6
GRAY_BACK = 7
BLACK_BACK = 8
PATH_START = 9

COLORS = {
    WALL: (0, 0, 0),
    SPACE: (255, 255, 255),
    START: (100, 100, 255),
    TARGET: (255, 0, 0),
    BLACK: (100, 100, 100),
    GRAY: (0, 255, 0),
    PATH: (255, 128, 255),
    GRAY_BACK: (128, 255, 128),
    BLACK_BACK: (64, 64, 64),
    PATH_START: (255, 255, 0)
}
