# tests/test_entry_point.py
import unittest

from solver import MazeAgent


class TestMazeEntryPoint(unittest.TestCase):
    """
    This class tests the find_starting_coordinates method with a number of
    different mazes.
    """
    def test_short_single_row_maze(self):
        maze = [[1, 1, 0, 1, 1]]
        maze_agent = MazeAgent(maze)
        self.assertEqual(
            maze_agent.maze_start, (2, 0), "Entry Point should be (2, 0)")

    def test_long_single_row_maze(self):
        maze = [[1, 1, 1, 1, 1, 1, 0, 1, 1, 1]]
        maze_agent = MazeAgent(maze)
        self.assertEqual(
            maze_agent.maze_start, (6, 0), "Entry Point should be (6, 0)")

    def test_multi_entry_single_row_maze(self):
        maze = [[1, 1, 1, 0, 1, 1, 1, 0, 1, 1]]
        maze_agent = MazeAgent(maze)
        self.assertEqual(
            maze_agent.maze_start, (3, 0), "Entry Point should be (3, 0)")

    def test_short_2D_maze(self):
        maze = [
            [1, 1, 0, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 0, 1, 1],
        ]
        maze_agent = MazeAgent(maze)
        self.assertEqual(
            maze_agent.maze_start, (2, 0), "Entry Point should be (2, 0)")

    def test_long_2D_maze(self):
        maze = [
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        ]
        maze_agent = MazeAgent(maze)
        self.assertEqual(
            maze_agent.maze_start, (5, 0), "Entry Point should be (5, 0)")


if __name__ == '__main__':
    unittest.main()
