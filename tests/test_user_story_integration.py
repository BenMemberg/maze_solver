# tests/test_user_story_integration.py

import unittest

from agent import MazeAgent
from solver import load_maze


class TestUserStories(unittest.TestCase):

    def test_user_story_1(self):
        # Test loading in the maze
        expected_maze = [
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        maze_file = "mazes/user_story_1.csv"
        maze = load_maze(maze_file)
        self.assertEqual(maze, expected_maze, "Failed to load maze correctly!")

        # Test finding the maze entry point
        maze_agent = MazeAgent(maze)
        self.assertEqual(
            maze_agent.maze_start, (1, 0), "Entry Point should be (1, 0)")

        # Use the maze agent to find the maze exit coordinates
        maze_exit = maze_agent.find_exit()
        self.assertEqual(maze_exit, (1, 0), "Maze Exit should be (1, 0)")

        # Ensure the maze path is correct
        expected_path = [(1, 0)]
        self.assertEqual(
            maze_agent.maze_path, expected_path, "Wrong maze path!")

    def test_user_story_2(self):
        # Test loading in the maze
        expected_maze = [
            [1, 1, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 0, 1],
        ]
        maze_file = "mazes/user_story_2.csv"
        maze = load_maze(maze_file)
        self.assertEqual(maze, expected_maze, "Failed to load maze correctly!")

        # Test finding the maze entry point
        maze_agent = MazeAgent(maze)
        self.assertEqual(
            maze_agent.maze_start, (2, 0), "Entry Point should be (2, 0)")

        # Use the maze agent to find the maze exit coordinates
        maze_exit = maze_agent.find_exit()
        self.assertEqual(maze_exit, (2, 3), "Maze Exit should be (2, 3)")

        # Ensure the maze path is correct
        expected_path = [(2, 0), (2, 1), (2, 2), (2, 3)]
        self.assertEqual(
            maze_agent.maze_path, expected_path, "Wrong maze path!")

    def test_user_story_3(self):
        # Test loading in the maze
        expected_maze = [
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1],
        ]
        maze_file = "mazes/user_story_3.csv"
        maze = load_maze(maze_file)
        self.assertEqual(maze, expected_maze, "Failed to load maze correctly!")

        # Test finding the maze entry point
        maze_agent = MazeAgent(maze)
        self.assertEqual(
            maze_agent.maze_start, (1, 0), "Entry Point should be (1, 0)")

        # Use the maze agent to find the maze exit coordinates
        maze_exit = maze_agent.find_exit()
        self.assertEqual(maze_exit, (3, 3), "Maze Exit should be (3, 3)")

        # Ensure the maze path is correct
        expected_path = [(1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3)]
        self.assertEqual(
            maze_agent.maze_path, expected_path, "Wrong maze path!")

    def test_user_story_4(self):
        # Test loading in the maze
        expected_maze = [
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1],
        ]
        maze_file = "mazes/user_story_4.csv"
        maze = load_maze(maze_file)
        self.assertEqual(maze, expected_maze, "Failed to load maze correctly!")

        # Test finding the maze entry point
        maze_agent = MazeAgent(maze)
        self.assertEqual(
            maze_agent.maze_start, (1, 0), "Entry Point should be (1, 0)")

        # Use the maze agent to find the maze exit coordinates
        maze_exit = maze_agent.find_exit()
        self.assertEqual(maze_exit, (3, 6), "Maze Exit should be (3, 6)")

        # Ensure the maze path is correct
        expected_path = [
            (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3),
            (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (3, 6)
        ]
        self.assertEqual(
            maze_agent.maze_path, expected_path, "Wrong maze path!")

    def test_user_story_5(self):
        # Test loading in the maze
        expected_maze = [
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1],

        ]
        maze_file = "mazes/user_story_5.csv"
        maze = load_maze(maze_file)
        self.assertEqual(maze, expected_maze, "Failed to load maze correctly!")

        # Test finding the maze entry point
        maze_agent = MazeAgent(maze)
        self.assertEqual(
            maze_agent.maze_start, (1, 0), "Entry Point should be (1, 0)")

        # Use the maze agent to find the maze exit coordinates
        maze_exit = maze_agent.find_exit()
        self.assertEqual(maze_exit, (3, 5), "Maze Exit should be (3, 5)")

        # Ensure the maze path is correct
        expected_path = [
            (1, 0), (1, 1), (1, 2), (1, 3),
            (2, 3), (3, 3), (3, 4), (3, 5)
        ]
        self.assertEqual(
            maze_agent.maze_path, expected_path, "Wrong maze path!")

    def test_full_maze(self):
        # Test loading in the maze
        expected_maze = [
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
        maze_file = "mazes/full_maze.csv"
        maze = load_maze(maze_file)
        self.assertEqual(maze, expected_maze, "Failed to load maze correctly!")

        # Test finding the maze entry point
        maze_agent = MazeAgent(maze)
        self.assertEqual(
            maze_agent.maze_start, (4, 0), "Entry Point should be (4, 0)")

        # Use the maze agent to find the maze exit coordinates
        maze_exit = maze_agent.find_exit()
        self.assertEqual(maze_exit, (7, 9), "Maze Exit should be (7, 9)")

        # Ensure the maze path is correct
        expected_path = [
            (4, 0), (4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3), (3, 4),
            (3, 5), (4, 5), (5, 5), (5, 6), (5, 7), (5, 8), (6, 8), (7, 8),
            (7, 9)
        ]
        self.assertEqual(
            maze_agent.maze_path, expected_path, "Wrong maze path!")


if __name__ == '__main__':
    unittest.main()
