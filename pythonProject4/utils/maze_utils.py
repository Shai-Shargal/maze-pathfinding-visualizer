# utils/maze_utils.py

import pygame
import random
from .constants import *

class MazeCell:
    def __init__(self, row, col, parent=None):
        self.row = row
        self.col = col
        self.parent = parent

    def get_pos(self):
        return self.row, self.col

    def get_parent(self):
        return self.parent

def init_maze():
    maze = [[SPACE for _ in range(MAZE_SIZE)] for _ in range(MAZE_SIZE)]
    for i in range(MAZE_SIZE):
        maze[0][i] = WALL
        maze[MAZE_SIZE - 1][i] = WALL
        maze[i][0] = WALL
        maze[i][MAZE_SIZE - 1] = WALL

    for i in range(1, MAZE_SIZE - 1):
        for j in range(1, MAZE_SIZE - 1):
            if i % 2 == 1:
                maze[i][j] = WALL if random.randint(0, 9) < 2 else SPACE
            else:
                maze[i][j] = WALL if random.randint(0, 9) < 6 else SPACE

    start_row, start_col = MAZE_SIZE // 2, MAZE_SIZE // 2
    maze[start_row][start_col] = START

    while True:
        target_row = random.randint(0, MAZE_SIZE - 1)
        target_col = random.randint(0, MAZE_SIZE - 1)
        if maze[target_row][target_col] == SPACE:
            maze[target_row][target_col] = TARGET
            break

    return maze

def draw_maze(screen, maze):
    for row in range(MAZE_SIZE):
        for col in range(MAZE_SIZE):
            cell_value = maze[row][col]

            if isinstance(cell_value, tuple):
                cell_type, fade_step = cell_value
                base_color = COLORS.get(cell_type, (0, 255, 0))
                fade_amount = min(255, 50 + fade_step * 20)
                color = (base_color[0], max(0, base_color[1] - fade_step * 15), base_color[2])
                maze[row][col] = (cell_type, fade_step + 1)

                if fade_step > 10:
                    maze[row][col] = BLACK
            else:
                cell_type = cell_value
                color = COLORS.get(cell_type, (200, 200, 200))

            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)

def draw_text(screen, text, x, y, size=24):
    font = pygame.font.SysFont("arial", size)
    surface = font.render(text, True, (255, 255, 255))
    screen.blit(surface, (x, y))
