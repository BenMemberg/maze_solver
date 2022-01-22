# utils.py


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
