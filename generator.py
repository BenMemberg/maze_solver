# generator.py

import random
import argparse

from utils import print_maze
from constants import WALL, OPEN, UNVISITED


def count_adj_open_cells(maze, rand_wall):
    """
    Counts the number of spaces adjacent to the given space that have been marked as open cells.

    Returns the count of open spaces next to the target.
    """
    wall_y, wall_x = rand_wall
    open_cells = 0
    if (maze[wall_y - 1][wall_x] == OPEN):
        open_cells += 1
    if (maze[wall_y + 1][wall_x] == OPEN):
        open_cells += 1
    if (maze[wall_y][wall_x - 1] == OPEN):
        open_cells += 1
    if (maze[wall_y][wall_x + 1] == OPEN):
        open_cells += 1

    return open_cells

def mark_wall(maze, walls, target):
    """
    Marks the target space as a cell if it has not already been marked as an open cell.

    Additionally ensures the target space is in the active walls array.

    Returns the modified maze matrix and walls array.
    """
    if (maze[target[0]][target[1]] != OPEN):
        maze[target[0]][target[1]] = WALL
    if (target not in walls):
        walls.append(target)
    return maze, walls

def set_entrance(maze):
    """
    Sets an entry point to the given maze in the first row. The entry will connect to a random
    open space in the next row of the maze.

    Returns the given maze with an added entry point.
    """
    # Filter open spaces in the second row while maintaining their original indices
    entry_options = list(filter( lambda x: x[1] == OPEN, enumerate(maze[1])))
    # choose a random open space to be the entry point
    rand_i = int(random.random() * len(entry_options))
    entry_x = entry_options[rand_i][0]
    # Set entry point in the opening row
    maze[0][entry_x] = OPEN

    return maze

def set_exit(maze):
    """
    Sets an exit point to the given maze in the last row. The exit will connect to a random
    open space in the previous row of the maze.

    Returns the given maze with an added exit.
    """
    # Filter open spaces in the second to last row while maintaining their original indices
    exit_options = list(filter( lambda x: x[1] == OPEN, enumerate(maze[len(maze) - 2])))
    # choose a random open space to be the entry point
    rand_i = int(random.random() * len(exit_options))
    exit_x = exit_options[rand_i][0]
    # Set exit space in the last row
    maze[len(maze) - 1][exit_x] = OPEN

    return maze
