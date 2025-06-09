# algorithms/bfs.py

from collections import deque
from utils.constants import *
from utils.maze_utils import MazeCell

def bfs_generator(maze):
    visited = [[False for _ in range(MAZE_SIZE)] for _ in range(MAZE_SIZE)]
    start_cell = MazeCell(MAZE_SIZE // 2, MAZE_SIZE // 2)
    queue = deque([start_cell])

    while queue:
        cell = queue.popleft()
        r, c = cell.get_pos()

        if maze[r][c] == TARGET:
            yield 'found', cell
            return

        if maze[r][c] != START:
            maze[r][c] = (GRAY, 0)

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < MAZE_SIZE and 0 <= nc < MAZE_SIZE:
                if not visited[nr][nc] and maze[nr][nc] not in [WALL, GRAY, BLACK, START]:
                    visited[nr][nc] = True
                    queue.append(MazeCell(nr, nc, cell))

        if maze[r][c] != START:
            maze[r][c] = BLACK

        yield 'step', None

    yield 'not_found', None
