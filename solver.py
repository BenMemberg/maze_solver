# solver.py
import csv
import argparse

from agent import MazeAgent
from generator import generate_maze


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
        '--maze-file', '-f',
        required=False,
        default='mazes/full_maze.csv',
        help=('The .csv file containing the maze data. '
              'Check out the mazes/ folder for examples.'))
    parser.add_argument(
        '--maze-size', '-m',
        required=False,
        help='The width by height dimension (in the form "WxH") to use to generate a maze.')
    parser.add_argument(
        '--timeout', '-t',
        required=False,
        default=1000,
        help=('The timeout setting for the maze solver. The default of '
              '1000 should be sufficient for simple 10x10 mazes.'))

    args = parser.parse_args()

    if args.maze_size:
        width, height = [int(i) for i in args.maze_size.split('x')]
        print(f"Generating a ({width}x{height}) Maze")
        maze = generate_maze(width, height)
    else:
        print(f"Loading maze from the file: {args.maze_file}")
        maze = load_maze(args.maze_file)


    maze_agent = MazeAgent(maze)

    print("Initial Maze:")
    maze_agent.print_maze_state()

    print(f"Maze Entry Found: {maze_agent.maze_start}")

    maze_exit = maze_agent.find_exit(args.timeout)
    print(f"Maze Exit Found: {maze_agent.maze_exit}")
    print("\nMaze Solution:")
    maze_agent.print_maze_state()
    print("Solution Path: \n" + str(maze_agent.maze_path))
