# algorithms/dfs.py

from utils.constants import *
from utils.maze_utils import MazeCell

def dfs_generator(maze):
    visited = [[False for _ in range(MAZE_SIZE)] for _ in range(MAZE_SIZE)]

    def dfs(r, c, parent):
        if not (0 <= r < MAZE_SIZE and 0 <= c < MAZE_SIZE):
            return None
        if visited[r][c] or maze[r][c] == WALL:
            return None

        visited[r][c] = True
        cell = MazeCell(r, c, parent)

        if maze[r][c] == TARGET:
            return cell

        if maze[r][c] not in [START, TARGET]:
            maze[r][c] = (GRAY, 0)
            yield 'step', None  # נכנסנו לתא

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            result = yield from dfs(r + dr, c + dc, cell)
            if isinstance(result, MazeCell):
                return result  # מצאנו יעד → יוצאים

        # לא מצאנו → חוזרים אחורה
        if maze[r][c] not in [START, TARGET]:
            maze[r][c] = (BLACK_BACK, 0)
            yield 'step', None  # צעד חזרה

        return None

    result = yield from dfs(MAZE_SIZE // 2, MAZE_SIZE // 2, None)
    if isinstance(result, MazeCell):
        yield 'found', result
    else:
        yield 'not_found', None
