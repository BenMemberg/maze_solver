# tests/test_maze_agent.py
import unittest

from agent import MazeAgent


class TestMazeAgent(unittest.TestCase):
    """
    This class tests the supporting instance methods of the MazeAgent class.
    """
    def setUp(self):
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
        self.maze_agent = MazeAgent(self.maze)
        self.step = 1

    def test_zeros_matrix_short(self):
        # Test zeros_matrix method with a non-symmetrical dimension of 4x3
        expected_zeros_matrix_short = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        zeros_matrix_short = self.maze_agent.zeros_matrix(4, 3)
        self.assertEqual(
            zeros_matrix_short,
            expected_zeros_matrix_short,
            "Zeros matrix genererated incorrectly!")

    def test_zeros_matrix_short_full(self):
        # Test zeros_matrix method with a full size matrix (len/width of
        # self.maze).
        expected_zeros_matrix_full = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        zeros_matrix_full = self.maze_agent.zeros_matrix(
                                len(self.maze[0]), len(self.maze))
        self.assertEqual(
            zeros_matrix_full,
            expected_zeros_matrix_full,
            "Zeros matrix genererated incorrectly!")
