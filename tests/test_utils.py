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
