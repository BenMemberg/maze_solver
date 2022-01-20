#!/usr/bin/env python
import csv
import argparse


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


if __name__ == '__main__':

    # parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--maze-file', '-m',
        required=True,
        help='The .csv file containing the maze data.')

    args = parser.parse_args()

    maze = load_maze(args.maze_file)
