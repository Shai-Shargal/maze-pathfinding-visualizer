# algorithms/ids.py

from utils.constants import *
from utils.maze_utils import MazeCell

def ids_generator(maze):
    def dls(r, c, depth, visited, parent, limit):
        if not (0 <= r < MAZE_SIZE and 0 <= c < MAZE_SIZE):
            return None
        if maze[r][c] == WALL or visited[r][c] or depth > limit:
            return None

        visited[r][c] = True
        cell = MazeCell(r, c, parent)

        if maze[r][c] == TARGET:
            return cell

        if maze[r][c] not in [START, TARGET]:
            maze[r][c] = (GRAY, 0)
            yield 'step', None  # נכנסנו לתא

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            result = yield from dls(r + dr, c + dc, depth + 1, visited, cell, limit)
            if isinstance(result, MazeCell):
                return result


        if maze[r][c] not in [START, TARGET]:
            maze[r][c] = (BLACK_BACK, 0)
            yield 'step', None

        return None

    max_depth = MAZE_SIZE * MAZE_SIZE
    for limit in range(1, max_depth):
        visited = [[False for _ in range(MAZE_SIZE)] for _ in range(MAZE_SIZE)]
        result = yield from dls(MAZE_SIZE // 2, MAZE_SIZE // 2, 0, visited, None, limit)
        if isinstance(result, MazeCell):
            yield 'found', result
            return
        yield 'step', None

    yield 'not_found', None
