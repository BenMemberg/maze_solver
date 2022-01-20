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


def format_maze(maze):
    """
    Converts a maze from matrix format to ASCII graphical format for output.
    """
    maze_str = ""
    for row in maze:
        maze_str += format_row(row)
        maze_str += "\n"
    return maze_str
