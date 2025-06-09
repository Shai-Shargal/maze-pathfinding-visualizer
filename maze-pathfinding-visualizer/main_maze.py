# main.py

import pygame
from utils.maze_utils import init_maze, draw_maze, draw_text, MazeCell
from utils.constants import *
from algorithms.bfs import bfs_generator
from algorithms.dfs import dfs_generator
from algorithms.ids import ids_generator
from algorithms.bidirectional import bidirectional_bfs_generator


def reconstruct_path(maze, end_cell):
    while end_cell:
        r, c = end_cell.get_pos()
        if maze[r][c] not in [START, TARGET]:
            maze[r][c] = PATH
        end_cell = end_cell.get_parent()

def main_menu(screen):
    screen.fill((0, 0, 0))
    draw_text(screen, "Maze Search Visualization", 140, 100, size=36)
    draw_text(screen, "Press 1 for BFS", 200, 200)
    draw_text(screen, "Press 2 for IDS", 200, 250)
    draw_text(screen, "Press 3 for DFS", 200, 300)
    draw_text(screen, "Press 4 for Bidirectional BFS", 200, 350)
    draw_text(screen, "Press R to generate a new maze", 200, 400)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 'bfs'
                elif event.key == pygame.K_2:
                    return 'ids'
                elif event.key == pygame.K_3:
                    return 'dfs'
                elif event.key == pygame.K_4:
                    return 'bidirectional'
                elif event.key == pygame.K_r:
                    return 'restart'

def main():
    pygame.init()
    EXTRA_HEIGHT = 40
    screen = pygame.display.set_mode((MAZE_SIZE * CELL_SIZE, MAZE_SIZE * CELL_SIZE + EXTRA_HEIGHT))
    pygame.display.set_caption("Maze Search Visualization")
    clock = pygame.time.Clock()

    while True:
        algo = main_menu(screen)
        if algo is None:
            break

        maze = init_maze()
        generator = {
            'bfs': bfs_generator,
            'dfs': dfs_generator,
            'ids': ids_generator,
            'bidirectional': bidirectional_bfs_generator
        }[algo](maze)

        running = True
        path_found = None

        while running:
            screen.fill((128, 128, 128))
            draw_maze(screen, maze)
            draw_text(screen, f"Algorithm: {algo.upper()} (Press R to Restart, ESC to Quit)", 10,
                      MAZE_SIZE * CELL_SIZE + 5, 18)
            pygame.display.flip()
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        running = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return

            try:
                result, data = next(generator)
                if result == 'found':
                    path_found = data
                    reconstruct_path(maze, path_found)

                    showing_path = True
                    while showing_path:
                        screen.fill((128, 128, 128))
                        draw_maze(screen, maze)
                        draw_text(screen, f"Path found with {algo.upper()}. Press R to restart, ESC to quit.", 10,
                                  MAZE_SIZE * CELL_SIZE + 5, 18)
                        pygame.display.flip()
                        clock.tick(60)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                showing_path = False
                                running = False
                                return
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_r:
                                    showing_path = False
                                    running = False
                                elif event.key == pygame.K_ESCAPE:
                                    pygame.quit()
                                    return
                    break
                elif result == 'not_found':
                    break
            except StopIteration:
                break

    pygame.quit()

if __name__ == "__main__":
    main()
