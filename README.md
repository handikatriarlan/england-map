# England Map - Pathfinding Algorithms

<p align="center">
    <img src="https://ucarecdn.com/cafff42d-77d7-4a02-a8a7-72ff49010f4c/englandmap.png" width="400" alt="England Map Graph">
</p>

This repository contains the implementation of various pathfinding algorithms (BFS, DFS, Greedy Best-First Search, and A\*) using the AIMA Python library. These algorithms are applied to an undirected graph representation of locations on a map (England map example).

## Algorithms Implemented

- **Breadth-First Search (BFS)**: Explores all nodes at the present depth before moving on to nodes at the next depth level.
- **Depth-First Search (DFS)**: Explores as far as possible along each branch before backtracking.
- **Greedy Best-First Search**: Uses a heuristic to prioritize which nodes to explore based on estimated cost to the goal.
- **A-Star (A\*) Search**: Combines the features of Greedy Best-First Search and Uniform-Cost Search, utilizing both actual cost and estimated cost to find the optimal path.

## Features

- Implementations using the AIMA Python library for simplicity and readability.
- Support for various graph-based search strategies.
- Custom map data for representing real-world locations.

## Usage

To run the project, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/handikatriarlan/england-map.git
   cd england-map
   ```

2. Run any of the algorithms, e.g. for bfs algorithm:
   ```bash
   python bfs-aima.py
   ```

## Code Examples

### Breadth-First Search (BFS)

```python
from search import breadth_first_tree_search

result = breadth_first_graph_search(england_problem)
print(result.solution())
```

### Depth-First Search (DFS)

```python
from search import depth_first_tree_search

result = depth_first_graph_search(england_problem)
print(result.solution())
```

### Greedy Best-First Search

```python
from search import greedy_best_first_graph_search

result = greedy_best_first_graph_search(england_problem, lambda node: england_problem.h(node))
print(result.solution())
```

### A-Star (A\*)

```python
from search import astar_search

result = astar_search(england_problem, lambda node: england_problem.h(node))
print(result.solution())
```
