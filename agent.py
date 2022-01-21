# agent.py

from utils import format_maze, format_row


class MazeAgent(object):
    """
    A class that holds the data and methods needed for an agent to navigate a
    given maze.
    """
    def __init__(self, maze):
        # Initialize maze data from args
        self.maze = maze
        self.start_row, self.start_col = self.find_maze_start()

        # Initialize agent's route matrix
        self.routes = self.zeros_matrix(len(maze[0]), len(maze))
        self.routes[self.start_col][self.start_row] = 1

    def __str__(self):
        return format_maze(self.maze)

    @property
    def maze_start(self):
        """
        Returns the coordinates of the maze start as a tuple.
        """
        return (self.start_row, self.start_col)

    def find_maze_start(self):
        """
        Finds the coordinate of the entrance to the maze. If there is more than
        one entrance, returns the first entry coordinates found.
        """
        entry_row = self.maze[0]
        for point, val in enumerate(entry_row):
            if val == 0:
                return (point, 0)
        raise ValueError(
            "Entry not found! Entry row given:\n" + format_row(entry_row))

    def zeros_matrix(self, width, length):
        """
        Returns a matrix of zeros with the given dimensions.
        """
        zeros = []
        for i in range(length):
            zeros.append([0 for j in range(width)])
        return zeros