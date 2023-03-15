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
        # Call instance method to find the maze's starting coordinates
        self.start_row, self.start_col = self.find_maze_start()
        self.location = {
            'front': [],
            'center': [],
            'back': []
        }
        self.step = 0
        # Initialize the class attributes tha trepresent the maze solution
        self.maze_path = []
        self.exit_row, self.exit_col = None, None

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

    def evaluate_coord(self, row, col):
        """
        Evaluates the given coordinate to see if it is a wall or open space.

        Returns True if the coordinate is open space, False if it is a wall.
        """
        # Ensure the given coordinate is within the maze bounds
        if (row < 0 or row >= len(self.maze[0]) or
                col < 0 or col >= len(self.maze)):
            return False

        # Ensure the agent isn't trying to navigate backwards
        if (self.routes[col][row] > 0 and self.routes[col][row] != self.step):
            return False

        # Return True if the coordinate is to an open space
        return self.maze[col][row] == 0

    def evaluate_location(self, x_shift, y_shift):
        """
        Evaluates the given coordinate to see if it is a wall or open space.

        Returns True if the coordinate is open space, False if it is a wall.
        """
        return (self.evaluate_coord(self.location['front'][0] + 1, self.location['front'][1]) and
                self.evaluate_coord(self.location['center'][0] + 1, self.location['center'][1]) and
                self.evaluate_coord(self.location['back'][0] + 1, self.location['back'][1]))

    def agent_at_exit(self):
        """
        Evaluates a given tuple location to determine if the agent is at the
        maze exit. A maze exit must be a valid open coordinate and it must be
        in the final row of the maze.
        """
        front_valid = self.evaluate_coord(self.location['front'][0], self.location['front'][1])
        center_valid = self.evaluate_coord(self.location['center'][0], self.location['center'][1])
        back_valid = self.evaluate_coord(self.location['back'][0], self.location['back'][1])
        return (
            front_valid and center_valid and back_valid and
            self.location['front'][1] == (len(self.maze) - 1))

    def enter_maze(self):
        """
        Evaluates a given tuple location to determine if the agent is at the
        maze exit. A maze exit must be a valid open coordinate and it must be
        in the final row of the maze.
        """
        # Check back coord
        if (self.evaluate_coord(self.start_row, self.start_col)):
            self.location['back'] = [self.start_row, self.start_col]

        # check center coord
        if (self.evaluate_coord(self.start_row, self.start_col + 1)):
            self.location['center'] = [self.start_row, self.start_col + 1]

        # check front coord
        if (self.evaluate_coord(self.start_row, self.start_col + 2)):
            self.location['front'] = [self.start_row, self.start_col + 2]

        self.maze_path.append(self.maze_start)

    def find_exit(self, timeout=1000):
        """
        This method navigates the maze and fills out self.routes until it
        finds the exit of the maze or times out. A maze exit is defined by
        an open space in the final row of the maze.
        """
        time = 0
        self.step = 1
        self.enter_maze()
        while time < timeout:
            # Mark current position
            self.routes[self.location['center'][1]][self.location['center'][0]] = self.step
            self.maze_path.append((self.location['center'][0], self.location['center'][1]))
            # Check if current position is an exit
            if self.agent_at_exit(location):
                self.exit_row = self.location['front'][0]
                self.exit_col = self.location['front'][1]
                self.maze_path.append(self.maze_exit)
                return self.maze_exit
            # Evaluate one space below the current agent location
            elif self.evaluate_location(0, 1):
                # If the space is open, advance the location
                location[1] += 1
                self.step += 1
            # Evaluate one space to the right of current agent location
            elif self.evaluate_location(1, 0):
                # If the space is open, advance the location
                location[0] += 1
                self.step += 1
            # Evaluate one space to the left of current agent location
            elif self.evaluate_location(-1, 0):
                # If the space is open, advance the location
                location[0] -= 1
                self.step += 1
            # Evaluate one space above the current agent location
            elif self.evaluate_location(0, -1):
                # If the space is open, advance the location
                location[1] -= 1
                self.step += 1
            else:
                # Remove current location from maze path
                self.maze_path.pop()
                # Remove the prior location from the maze path and set it to
                # the current location (It will be re-added on the next loop).
                location = list(self.maze_path.pop())
                # Decrement current step
                self.step -= 1
            time += 1
        raise TimeoutError("Maze solver timed out while searching for exit!")
