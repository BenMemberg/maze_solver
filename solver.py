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


if __name__ == '__main__':

    # parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--maze-file', '-m',
        required=True,
        help='The .csv file containing the maze data.')

    args = parser.parse_args()

    maze = load_maze(args.maze_file)
    print("Maze Provided:\n" + format_maze(maze))

    maze_start = find_starting_coordinates(maze)
    print("Maze Entry: " + str(maze_start))
