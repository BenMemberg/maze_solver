# solver.py
import csv
import argparse

from agent import MazeAgent
from utils import format_maze


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
        required=False,
        default='mazes/full_maze.csv',
        help=('The .csv file containing the maze data. '
              'Check out the mazes/ folder for examples.'))

    args = parser.parse_args()

    maze = load_maze(args.maze_file)
    print("Maze Provided:\n" + format_maze(maze))

    maze_agent = MazeAgent(maze)
    print(f"Maze Entry: {maze_agent.maze_start}")

    maze_exit = maze_agent.find_exit()
