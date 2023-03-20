# utils.py

from colorama import  Fore, init
from constants import WALL, OPEN, UNVISITED

def format_row(row):
    """
    Converts a maze row from list format to ASCII graphical format for output.
    """
    row_str = ""
    for val in row:
        char = " # " if val == 1 else "   "
        row_str += char
    return row_str


def format_maze(maze, maze_path=[]):
    """
    Converts a maze, and optionally a solution path (list of coordinates),
    from matrix format to ASCII graphical format for output.
    """
    maze_str = ""
    for j, row in enumerate(maze):
        row_str = ""
        for i, val in enumerate(row):
            if val == 1:
                char = " # "
            elif (i, j) in maze_path:
                char = " x "
            else:
                char = "   "
            row_str += char
        maze_str += row_str
        maze_str += "\n"
    return maze_str

def print_maze(maze):
    """
    Prints out a given matrix in colored ASCII format. Can be used before, during, or
    after maze generation.
    """
    init()
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            if (maze[i][j] == UNVISITED):
                print(Fore.WHITE + 'U', end="  ")
            elif (maze[i][j] == OPEN):
                # print(Fore.GREEN + ' ', end="  ")
                print(Fore.BLACK + '0', end="  ")
                # print(Fore.GREEN + 'O', end="  ")
            elif (maze[i][j] == WALL):
                print(Fore.RED + '#', end="  ")
            else:
                print(Fore.MAGENTA + str(maze[i][j]), end="  ")
            
        print(Fore.WHITE + '\n')
