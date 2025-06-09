# algorithms/bidirectional.py

from collections import deque
from utils.constants import *
from utils.maze_utils import MazeCell

def bidirectional_bfs_generator(maze):
    start_pos = (MAZE_SIZE // 2, MAZE_SIZE // 2)
    target_pos = None

    for r in range(MAZE_SIZE):
        for c in range(MAZE_SIZE):
            if maze[r][c] == TARGET:
                target_pos = (r, c)
                break
        if target_pos:
            break

    visited_start = {}
    visited_target = {}

    queue_start = deque([MazeCell(*start_pos)])
    queue_target = deque([MazeCell(*target_pos)])

    visited_start[start_pos] = MazeCell(*start_pos)
    visited_target[target_pos] = MazeCell(*target_pos)

    meet_point = None

    while queue_start and queue_target:
        if queue_start:
            cell = queue_start.popleft()
            r, c = cell.get_pos()

            if (r, c) in visited_target:
                meet_point = (r, c)
                break

            if maze[r][c] not in [START, TARGET]:
                maze[r][c] = (GRAY, 0)

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < MAZE_SIZE and 0 <= nc < MAZE_SIZE:
                    if maze[nr][nc] not in [WALL] and (nr, nc) not in visited_start:
                        next_cell = MazeCell(nr, nc, cell)
                        queue_start.append(next_cell)
                        visited_start[(nr, nc)] = next_cell

            if maze[r][c] not in [START, TARGET]:
                maze[r][c] = BLACK

            yield 'step', None

        if queue_target:
            cell = queue_target.popleft()
            r, c = cell.get_pos()

            if (r, c) in visited_start:
                meet_point = (r, c)
                break

            if maze[r][c] not in [START, TARGET]:
                maze[r][c] = (GRAY_BACK, 0)

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < MAZE_SIZE and 0 <= nc < MAZE_SIZE:
                    if maze[nr][nc] not in [WALL] and (nr, nc) not in visited_target:
                        next_cell = MazeCell(nr, nc, cell)
                        queue_target.append(next_cell)
                        visited_target[(nr, nc)] = next_cell

            if maze[r][c] not in [START, TARGET]:
                maze[r][c] = BLACK_BACK

            yield 'step', None

    if meet_point:
        path = []

        cell = visited_start[meet_point]
        while cell:
            path.append(cell)
            cell = cell.get_parent()
        for cell in reversed(path):
            r, c = cell.get_pos()
            if maze[r][c] not in [START, TARGET]:
                maze[r][c] = PATH

        cell = visited_target[meet_point].get_parent()
        while cell:
            r, c = cell.get_pos()
            if maze[r][c] not in [START, TARGET]:
                maze[r][c] = PATH
            cell = cell.get_parent()

        yield 'found', visited_start[meet_point]
    else:
        yield 'not_found', None
