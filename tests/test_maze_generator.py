# tests/test_entry_point.py
import unittest

from constants import OPEN, WALL, UNVISITED
from generator import count_adj_open_cells, mark_wall, set_entrance, set_exit, generate_maze


class TestMazeEntryPoint(unittest.TestCase):
    """
    This class tests the find_starting_coordinates method with a number of
    different mazes.
    """
    def setUp(self):
        self.maze = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
            [1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
            [1, 1, 0, 1, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        self.partial_maze = [
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1,  1,  1,  1, -1, -1, -1, -1, -1],
            [-1,  0,  0,  0,  0,  0,  1,  1, -1, -1],
            [-1,  0,  1,  1,  1,  0,  0,  0,  1, -1],
            [-1,  1, -1,  0,  0,  0,  1, -1, -1, -1],
            [-1, -1,  1,  0,  1,  1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        ]
        self.walls = [[2, 2], [2, 3], [2, 4], [4, 2], [4, 3], [4, 4]]

    def test_count_adj_open_cells(self):
        # Test count_adj_open_cells method with different spaces that have a different
        # number of zeros next to them.
        self.assertEqual(
            count_adj_open_cells(self.partial_maze, [1, 5]),
            0,
            "Incorrect number of adjacent open spaces returned by count_adj_open_cells()")
        self.assertEqual(
            count_adj_open_cells(self.partial_maze, [2, 1]),
            1,
            "Incorrect number of adjacent open spaces returned by count_adj_open_cells()")
        self.assertEqual(
            count_adj_open_cells(self.partial_maze, [4, 2]),
            2,
            "Incorrect number of adjacent open spaces returned by count_adj_open_cells()")
        self.assertEqual(
            count_adj_open_cells(self.partial_maze, [4, 4]),
            3,
            "Incorrect number of adjacent open spaces returned by count_adj_open_cells()")
        self.assertEqual(
            count_adj_open_cells(self.maze, [6, 4]),
            4,
            "Incorrect number of adjacent open spaces returned by count_adj_open_cells()")

    def test_mark_wall_valid_space(self):
        # Test mark_wall method with a valid, unvisited space
        self.assertEqual(self.partial_maze[3][8], UNVISITED, 'Partial maze not initialized as expected.')
        modified_maze, modified_walls = mark_wall(self.partial_maze, self.walls, [3, 8])
        self.assertEqual(modified_maze[3][8], WALL, 'Failed to successfully mark a wall.')
        self.assertTrue([3, 8] in modified_walls, 'Failed to add space to walls list.')

    def test_mark_wall_invalid_space(self):
        # Test mark_wall method with an already open wspace, which cannot be marked as a wall
        self.assertEqual(self.partial_maze[4][1], OPEN, 'Partial maze not initialized as expected.')
        modified_maze, modified_walls = mark_wall(self.partial_maze, self.walls, [4, 1])
        self.assertEqual(modified_maze[4][1], OPEN, 'Did not correctly identify an open space when marking a wall.')
        self.assertFalse([4, 1] in modified_walls, 'Erroneously added space to walls list.')

    def test_set_entrance(self):
        # Test that the set_entrance method successfully sets an opening in the first row
        self.assertFalse(OPEN in self.maze[0], 'Full maze not initialized as expected.')
        modified_maze = set_entrance(self.maze)
        self.assertTrue(OPEN in modified_maze[0], 'Failed to set entrance point.')

    def test_set_exit(self):
        # Test that the set_exit method successfully sets an opening in the last row
        self.assertFalse(OPEN in self.maze[len(self.maze) - 1], 'Full maze not initialized as expected.')
        modified_maze = set_exit(self.maze)
        self.assertTrue(OPEN in modified_maze[len(modified_maze) - 1], 'Failed to set exit point.')

    def test_generate_maze(self):
        # Test generate_maze method creates a matrix of the correct dimensions
        generated_maze = generate_maze(15, 10)
        self.assertEqual(len(generated_maze), 10, 'Maze was generated with the wrong height.')
        self.assertEqual(len(generated_maze[0]), 15, 'Maze was generated with the wrong width.')

if __name__ == '__main__':
    unittest.main()
