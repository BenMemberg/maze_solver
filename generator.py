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

def generate_maze(width, height):
    """
    Generates a maze in matrix format with the given width and height. In this format walls are
    represented by 1s and open cells are represented by 0s.

    Uses "Randomized Prim's Algorithm" to generate the maze. For more info visit following link:
    https://en.wikipedia.org/wiki/Maze_generation_algorithm

    Returns a 2D matrix representation of the maze.
    """
    maze = []
    walls = []

    # Mark all cells as unvisited
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append(UNVISITED)
        maze.append(line)

    # Randomize starting point (excluding the maze edge spaces)
    starting_height = int(random.random() * (height - 2)) + 1
    starting_width = int(random.random() * (width - 2)) + 1

    # Mark starting cell as open and surrounding walls as walls
    maze[starting_height][starting_width] = OPEN
    # ORDER: UP,DOWN,LEFT,RIGHT
    maze[starting_height - 1][starting_width] = WALL
    maze[starting_height + 1][starting_width] = WALL
    maze[starting_height][starting_width - 1] = WALL
    maze[starting_height][starting_width + 1] = WALL

    # add surrounding walls to the walls list
    walls.append([starting_height - 1, starting_width])
    walls.append([starting_height + 1, starting_width])
    walls.append([starting_height, starting_width - 1])
    walls.append([starting_height, starting_width + 1])

    while (walls):
        # Pick a random wall
        rand_wall = walls[int(random.random()*len(walls))-1]

        # Check if the random wall meets the following condition:
        #   U        Key: (O=Open, W=Wall, U=Unvisited)
        # U W O
        #   U
        # and is not on the left maze wall
        if (rand_wall[1] != 0 and
                maze[rand_wall[0]][rand_wall[1]-1] == UNVISITED and
                maze[rand_wall[0]][rand_wall[1]+1] == OPEN):
            # Find the number of surrounding open cells
            open_cells = count_adj_open_cells(maze, rand_wall)
            if (open_cells < 2):
                # Change the wall space to an open cell space
                maze[rand_wall[0]][rand_wall[1]] = OPEN

                # Mark the walls of the newly marked open cell
                # Upper cell
                if (rand_wall[0] != 0):
                    maze, walls = mark_wall(maze, walls, [rand_wall[0] - 1, rand_wall[1]])

                # Bottom cell
                if (rand_wall[0] != height-1):
                    maze, walls = mark_wall(maze, walls, [rand_wall[0] + 1, rand_wall[1]])

                # Leftmost cell
                if (rand_wall[1] != 0):
                    maze, walls = mark_wall(maze, walls, [rand_wall[0], rand_wall[1] - 1])
            # Remove processed wall from walls list
            walls.remove(rand_wall)
            continue
        
        # Check if the random wall meets the following condition:
        #   U        Key: (O=Open, W=Wall, U=Unvisited)
        # U W U
        #   O
        # and is not on the upper maze wall
        if (rand_wall[0] != 0 and
                maze[rand_wall[0]-1][rand_wall[1]] == UNVISITED and
                maze[rand_wall[0]+1][rand_wall[1]] == OPEN):
            # Find the number of surrounding cells
            open_cells = count_adj_open_cells(maze, rand_wall)
            if (open_cells < 2):
                # Change the wall space to an open cell space
                maze[rand_wall[0]][rand_wall[1]] = OPEN

                # Mark the walls of the newly marked open cell
                # Upper cell
                if (rand_wall[0] != 0):
                    maze, walls = mark_wall(maze, walls, [rand_wall[0] - 1, rand_wall[1]])

                # Left cell
                if (rand_wall[1] != 0):
                    maze, walls = mark_wall(maze, walls, [rand_wall[0], rand_wall[1] - 1])

                # Right cell
                if (rand_wall[1] != width - 1):
                    maze, walls = mark_wall(maze, walls, [rand_wall[0], rand_wall[1] + 1])
            # Remove processed wall from walls list
            walls.remove(rand_wall)
            continue

        # Check if the random wall meets the following condition:
        #   O        Key: (O=Open, W=Wall, U=Unvisited)
        # U W U
        #   U
        # and is not on the bottom maze wall
        if (rand_wall[0] != height-1 and
                maze[rand_wall[0]+1][rand_wall[1]] == UNVISITED and
                maze[rand_wall[0]-1][rand_wall[1]] == OPEN):
            # Find the number of surrounding cells
            open_cells = count_adj_open_cells(maze, rand_wall)
            if (open_cells < 2):
                # Change the wall space to an open cell space
                maze[rand_wall[0]][rand_wall[1]] = OPEN

                # Mark the walls of the newly marked open cell
                # Bottom cell
                if (rand_wall[0] != height - 1):
                    maze, walls = mark_wall(maze, walls, [rand_wall[0] + 1, rand_wall[1]])

                # Left cell
                if (rand_wall[1] != 0):
                    maze, walls = mark_wall(maze, walls, [rand_wall[0], rand_wall[1] - 1])

                # Right cell
                if (rand_wall[1] != width - 1):
                    maze, walls = mark_wall(maze, walls, [rand_wall[0], rand_wall[1] + 1])
            # Remove processed wall from walls list
            walls.remove(rand_wall)
            continue

        # Check if the random wall meets the following condition:
        #   U        Key: (O=Open, W=Wall, U=Unvisited)
        # O W U
        #   U
        # and is not on the right maze wall
        if (rand_wall[1] != width - 1 and
                maze[rand_wall[0]][rand_wall[1]+1] == UNVISITED and
                maze[rand_wall[0]][rand_wall[1]-1] == OPEN):
            # Find the number of surrounding cells
            open_cells = count_adj_open_cells(maze, rand_wall)
            if (open_cells < 2):
                # Change the wall space to an open cell space
                maze[rand_wall[0]][rand_wall[1]] = OPEN

                # Mark the walls of the newly marked open cell
                # Upper cell
                if (rand_wall[0] != 0):
                    maze, walls = mark_wall(maze, walls, [rand_wall[0] - 1, rand_wall[1]])

                # Bottom cell
                if (rand_wall[0] != height - 1):
                    maze, walls = mark_wall(maze, walls, [rand_wall[0] + 1, rand_wall[1]])

                # Right cell
                if (rand_wall[1] != width - 1):
                    maze, walls = mark_wall(maze, walls, [rand_wall[0], rand_wall[1] + 1])
            # Remove processed wall from walls list
            walls.remove(rand_wall)
            continue
        
        # If the processed random wall is still in the walls list, remove it
        if rand_wall in walls:
            walls.remove(rand_wall)
    
    # Mark the remaining unvisited cells as walls
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == UNVISITED):
                maze[i][j] = WALL

    # Set entrance and exit randomly in the entrance and exit rows
    maze = set_entrance(maze)
    maze = set_exit(maze)

    return maze

