# agent.py
from colorama import  Fore, init

from utils import format_maze, format_row
from constants import WALL, OPEN

class MazeAgent(object):
    """
    A class that holds the data and methods needed for an agent to navigate a
    given maze.
    """
    def __init__(self, maze):
        # Initialize maze data from args
        self.maze = maze
        # Call instance method to find the maze's starting coordinates
        self.start_row, self.start_col = self.find_maze_start()
        # Initialize the class attributes tha trepresent the maze solution
        self.maze_path = []
        self.exit_row, self.exit_col = None, None

        # Initialize agent's route matrix
        self.routes = self.zeros_matrix(len(maze[0]), len(maze))

    def __str__(self):
        return format_maze(self.maze)

    @property
    def maze_start(self):
        """
        Returns the coordinates of the maze start as a tuple.
        """
        return (self.start_row, self.start_col)

    @property
    def maze_exit(self):
        """
        Returns the coordinates of the maze start as a tuple.
        """
        return (self.exit_row, self.exit_col)

    def find_maze_start(self):
        """
        Finds the coordinate of the entrance to the maze. If there is more than
        one entrance, returns the first entry coordinates found.
        """
        entry_row = self.maze[0]
        for point, val in enumerate(entry_row):
            if val == OPEN:
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

    def evaluate_coord(self, row, col, curr_step):
        """
        Evaluates the given coordinate to see if it is a wall or open space.

        Returns True if the coordinate is open space, False if it is a wall.
        """
        # Ensure the given coordinate is within the maze bounds
        if (row < 0 or row >= len(self.maze[0]) or
                col < 0 or col >= len(self.maze)):
            return False

        # Ensure the agent isn't trying to navigate backwards
        if (self.routes[col][row] > 0 and self.routes[col][row] != curr_step):
            return False

        # Return True if the coordinate is to an open space
        return self.maze[col][row] == 0

    def agent_at_exit(self, location, curr_step):
        """
        Evaluates a given tuple location to determine if the agent is at the
        maze exit. A maze exit must be a valid open coordinate and it must be
        in the final row of the maze.
        """
        return (
            self.evaluate_coord(location[0], location[1], curr_step) and
            location[1] == (len(self.maze) - 1))

    def find_exit(self, timeout=1000):
        """
        This method navigates the maze and fills out self.routes until it
        finds the exit of the maze or times out. A maze exit is defined by
        an open space in the final row of the maze.
        """
        time = 0
        step = 1
        self.routes[self.start_col][self.start_row] = 1
        location = list(self.maze_start)
        while time < timeout:
            # Mark current position
            self.routes[location[1]][location[0]] = step
            self.maze_path.append((location[0], location[1]))
            # Check if current position is an exit
            if self.agent_at_exit(location, step):
                self.exit_row = location[0]
                self.exit_col = location[1]
                return self.maze_exit
            # Evaluate one space below the current agent location
            elif self.evaluate_coord(location[0], location[1] + 1, step):
                # If the space is open, advance the location
                location[1] += 1
                step += 1
            # Evaluate one space to the right of current agent location
            elif self.evaluate_coord(location[0] + 1, location[1], step):
                # If the space is open, advance the location
                location[0] += 1
                step += 1
            # Evaluate one space to the left of current agent location
            elif self.evaluate_coord(location[0] - 1, location[1], step):
                # If the space is open, advance the location
                location[0] -= 1
                step += 1
            # Evaluate one space above the current agent location
            elif self.evaluate_coord(location[0], location[1] - 1, step):
                # If the space is open, advance the location
                location[1] -= 1
                step += 1
            else:
                # Remove current location from maze path
                self.maze_path.pop()
                # Remove the prior location from the maze path and set it to
                # the current location (It will be re-added on the next loop).
                location = list(self.maze_path.pop())
                # Decrement current step
                step -= 1
            time += 1
        raise TimeoutError("Maze solver timed out while searching for exit!")

    def print_maze_state(self):
        """
        Prints out the current state of maze agent in the maze matrix in colored ASCII format.

        Walls are printed as a red '#', open un-visited spaces are printed as a black/gray '0',
        the solution path spaces are printed as a yellow 'X', and visited spaces that are not
        part of the solution path are printed as green 'V's.

        Returns nothing, outputs to the console.
        """
        init()
        for i in range(0, len(self.maze)):
            for j in range(0, len(self.maze[i])):
                if (j, i) in self.maze_path:
                    print(Fore.YELLOW + 'X', end="  ")
                elif (self.routes[i][j] > 0):
                    print(Fore.GREEN + 'V', end="  ")
                elif (self.maze[i][j] == OPEN):
                    print(Fore.BLACK + '0', end="  ")
                elif (self.maze[i][j] == WALL):
                    print(Fore.RED + '#', end="  ")
                else:
                    print(Fore.MAGENTA + str(self.maze[i][j]), end="  ")
            print(Fore.WHITE + '\n')
