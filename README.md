# InformedSearch-Algorithms-AI
This repository contains solutions to common problems using informed/heuristic search algorithms, created for an Artificial Intelligence course.

#Problem Description: 8-Puzzle

The 8-puzzle consists of a 3x3 grid with 8 numbered tiles (1 through 8) and one blank space that allows the tiles to be moved. The objective is to move the tiles around the grid by sliding them into the blank space until the tiles are arranged in a specific goal configuration.


**Initial State:** Any configuration of the tiles where only one tile can move into the blank space at a time. For example, a common initial state might be a scrambled arrangement of tiles.

**Goal State:** A particular configuration of tiles, often the tiles arranged in numerical order with the blank in the bottom-right corner:

![Initial-state-and-goal-state-of-8-puzzle](https://github.com/Sibgha-Zeeshan/InformedSearch-Algorithms-AI/assets/132210204/67b93a6f-b72a-470e-8e68-fdb3c246f2a3)

#Rules for solving the puzzle.

Instead of moving the tiles in the empty space, we can visualize moving the empty space in place of the tile, basically swapping the tile with the empty space. The empty space can only move in four directions viz.,

1. Up
2. Down
3. Right or
4. Left

The empty space cannot move diagonally and can take only one step at a time (i.e. move the empty space one position at a time).

# A* Algorithm

A* is a computer algorithm that is widely used in pathfinding and graph traversal, the process of plotting an efficiently traversable path between multiple points, called nodes. Noted for its performance and accuracy, it enjoys widespread use.
The key feature of the A* algorithm is that it keeps a track of each visited node which helps in ignoring the nodes that are already visited, saving a huge amount of time. It also has a list that holds all the nodes that are left to be explored and it chooses the most optimal node from this list, thus saving time not exploring unnecessary or less optimal nodes.
So we use two lists namely ‘open list‘ and ‘closed list‘ the open list contains all the nodes that are being generated and are not existing in the closed list and each node explored after it’s neighboring nodes are discovered is put in the closed list and the neighbors are put in the open list this is how the nodes expand. Each node has a pointer to its parent so that at any given point it can retrace the path to the parent. Initially, the open list holds the start(Initial) node. The next node chosen from the open list is based on its f score, the node with the least f score is picked up and explored.

**$fscore = hscore + gscore$**

A* uses a combination of heuristic value (h-score: how far the goal node is) as well as the g-score (i.e. the number of nodes traversed from the start node to current node).

In our 8-Puzzle problem, we can define the h-score as the number of misplaced tiles by comparing the current state and the goal state or summation of the Manhattan distance between misplaced nodes. g-score will remain as the number of nodes traversed from a start node to get to the current node.

# Hill Climbing

Hill climbing is a heuristic search algorithm used to solve problems like the 8-puzzle. It works  It starts from an initial state and iteratively moves to a neighboring state with a lower Manhattan distance. The process continues until it either reaches the goal state or gets stuck in a local optimum, where no neighbor has a better heuristic value. This basic version does not include mechanisms to escape local optima, such as random restarts or simulated annealing.

In the context of the 8-puzzle problem, A* is generally better than hill climbing because it uses both path cost and heuristic to find the optimal solution, whereas hill climbing is prone to getting stuck in local optima and may not find the goal state.
