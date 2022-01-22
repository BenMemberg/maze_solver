# tests/test_utils.py
import unittest

from utils import format_row, format_maze


class TestUtils(unittest.TestCase):
    """
    This class tests the utility display methods in utils.py.
    """
    def setUp(self) -> None:
        self.maze = [
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
            [1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
            [1, 1, 0, 1, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        ]
        self.partial_path = [
            (4, 0), (4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3), (3, 4)
        ]
        self.full_path = [
            (4, 0), (4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3), (3, 4),
            (3, 5), (4, 5), (5, 5), (5, 6), (5, 7), (5, 8), (6, 8), (7, 8),
            (7, 9)
        ]

    def test_format_row(self):
        expected_output = " #     #  #  #     #  #  #  # "
        formatted_row = format_row(self.maze[6])
        self.assertEqual(formatted_row, expected_output)

    def test_format_maze_no_path(self):
        formatted_maze = format_maze(self.maze)
        expected_output = (
            " #  #  #  #     #  #  #  #  # \n"
            " #                          # \n"
            " #     #  #  #     #  #     # \n"
            " #  #  #              #     # \n"
            " #           #  #  #  #     # \n"
            " #  #  #           #        # \n"
            " #     #  #  #     #  #  #  # \n"
            " #                 #  #     # \n"
            " #  #     #  #              # \n"
            " #  #  #  #  #  #  #     #  # \n")
        self.assertEqual(formatted_maze, expected_output)

    def test_format_maze_partial_path(self):
        formatted_maze = format_maze(self.maze, self.partial_path)
        expected_output = (
            " #  #  #  #  x  #  #  #  #  # \n"
            " #           x  x           # \n"
            " #     #  #  #  x  #  #     # \n"
            " #  #  #  x  x  x     #     # \n"
            " #        x  #  #  #  #     # \n"
            " #  #  #           #        # \n"
            " #     #  #  #     #  #  #  # \n"
            " #                 #  #     # \n"
            " #  #     #  #              # \n"
            " #  #  #  #  #  #  #     #  # \n")
        self.assertEqual(formatted_maze, expected_output)

    def test_format_maze_and_solution_path(self):
        formatted_maze = format_maze(self.maze, self.full_path)
        expected_output = (
            " #  #  #  #  x  #  #  #  #  # \n"
            " #           x  x           # \n"
            " #     #  #  #  x  #  #     # \n"
            " #  #  #  x  x  x     #     # \n"
            " #        x  #  #  #  #     # \n"
            " #  #  #  x  x  x  #        # \n"
            " #     #  #  #  x  #  #  #  # \n"
            " #              x  #  #     # \n"
            " #  #     #  #  x  x  x     # \n"
            " #  #  #  #  #  #  #  x  #  # \n")
        self.assertEqual(formatted_maze, expected_output)
