# tests.py

import unittest

from solver import load_maze, MazeAgent


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

if __name__ == '__main__':
    unittest.main()
