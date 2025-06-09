# Maze Pathfinding Visualizer

An interactive visualization tool for exploring classic AI search algorithms in a randomly generated maze.  
This project was developed as part of a course in Artificial Intelligence for Game Development.

## 🎯 Purpose

To demonstrate and compare different search algorithms visually, highlighting their behaviors and paths in real-time.

## 🚀 Features

- Random maze generation with start (blue) and goal (red) points
- Visualization of:
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Iterative Deepening Search (IDS)
  - Bidirectional BFS
- Real-time step-by-step animation
- Path highlighting upon reaching the target

## 🧠 Algorithms Used

| Algorithm         | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **BFS**          | Explores the maze layer by layer to find the shortest path                 |
| **DFS**          | Explores the deepest path first, with backtracking                         |
| **IDS**          | Combines DFS with breadth-wise depth limit increase                        |
| **Bidirectional**| Two BFS searches from start and target that meet in the middle             |

## 🖼️ Visual Representation

- **White**: Unvisited space
- **Black**: Walls
- **Blue**: Start point
- **Red**: Target point
- **Green / Gray**: Visited cells
- **Pink**: Final path
- **Dark Gray**: Backtracked cells

## 🛠 Technologies

- Python 3.x
- Pygame

## 📦 Installation

```bash
git clone https://github.com/your-username/maze-pathfinding-visualizer.git
cd maze-pathfinding-visualizer
pip install pygame
python main.py
