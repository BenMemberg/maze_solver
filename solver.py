# solver.py

import csv
import argparse

from utils import format_maze, format_row


def load_maze(maze_file):
    """
    Load maze file csv data into a list of lists, representing the maze
    in matrix format.
    """
    maze = []
    with open(maze_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            # Convert row data from list of strings to list of ints
            maze.append([int(i) for i in row])
    return maze

def find_starting_coordinates(maze):
    """
    Finds the coordinate of the entrance to the maze. If there is more than
    one entrance, returns the first entry coordinates found.
    """
    entry_row = maze[0]
    for point, val in enumerate(entry_row):
        if int(val)==0:
            return (point, 0)
    raise ValueError("Entry not found! Entry row given:\n" + format_row(entry_row))


class MazeAgent(object):
    """
    A class that holds the data and methods needed for an agent to navigate a
    given maze.
    """
    def __init__(self, maze, maze_start):
        # Initialize maze data from args
        self.maze = maze
        self.start_row, self.start_col = maze_start

        # Initialize agent's route matrix
        self.routes = self.zeros_matrix(len(maze[0]), len(maze))
        self.routes[self.start_col][self.start_row] = 1

    def zeros_matrix(self, width, length):
        """
        Returns a matrix of zeros with the given dimensions.
        """
        zeros = []
        for i in range(length):
            zeros.append([0 for j in range(width)])
        return zeros


if __name__ == '__main__':

    # parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--maze-file', '-m',
        required=False,
        default='mazes/full_maze.csv',
        help=('The .csv file containing the maze data. '
              'Check out the mazes/ folder for examples.'))

    args = parser.parse_args()

    maze = load_maze(args.maze_file)
    print("Maze Provided:\n" + format_maze(maze))

    maze_start = find_starting_coordinates(maze)
    print("Maze Entry: " + str(maze_start))

    maze_agent = MazeAgent(maze, maze_start)
