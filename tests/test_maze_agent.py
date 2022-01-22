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

    def test_evaluate_coord_new_spaces_first_row_wall(self):
        # Evaluate a wall in the first row
        self.assertFalse(self.maze_agent.evaluate_coord(2, 0, self.step))

    def test_evaluate_coord_new_spaces_first_row_open(self):
        # Evaluate the maze entry point
        self.assertTrue(self.maze_agent.evaluate_coord(4, 0, self.step))

    def test_evaluate_coord_new_spaces_hall_wall(self):
        # Evaluate a wall within the maze
        self.assertFalse(self.maze_agent.evaluate_coord(5, 4, self.step))

    def test_evaluate_coord_new_spaces_hall_open(self):
        # Evaluate an open space within the maze
        self.assertTrue(self.maze_agent.evaluate_coord(7, 5, self.step))

    def test_evaluate_coord_new_spaces_last_row_wall(self):
        # Evaluate a wall in the exit row
        self.assertFalse(self.maze_agent.evaluate_coord(5, 9, self.step))

    def test_evaluate_coord_new_spaces_last_row_open(self):
        # Evaluate the maze exit point
        self.assertTrue(self.maze_agent.evaluate_coord(7, 9, self.step))

    def test_evaluate_coord_already_traversed_equal_step(self):
        # Set maze agent traversed path data
        self.step = 5
        self.maze_agent.routes[3][5] = 5
        # Evaluate an open space that has been visted at the current step
        self.assertTrue(self.maze_agent.evaluate_coord(5, 3, self.step))

    def test_evaluate_coord_already_traversed_lower_step(self):
        # Set maze agent traversed path data
        self.step = 5
        self.maze_agent.routes[2][5] = 4
        # Evaluate an open space that has been visted before the current step
        self.assertFalse(self.maze_agent.evaluate_coord(5, 2, self.step))

    def test_evaluate_coord_already_traversed_higher_step(self):
        # Set maze agent traversed path data
        self.step = 5
        self.maze_agent.routes[3][4] = 6
        # Evaluate an open space that has been visted after the current step
        self.assertFalse(self.maze_agent.evaluate_coord(4, 3, self.step))
