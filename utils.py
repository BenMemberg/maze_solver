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

