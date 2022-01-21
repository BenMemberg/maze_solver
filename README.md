# Maze Solver

This project contains the code to solve a given maze file.

## How to use the maze solver

The main execution file for the project is solver.py. It takes an optional
argument "--maze-file" or "-m" which should be the path from the project folder
to the target maze file to solve. If the maze file argument is not provided,
the solver will use the file "mazes/full_maze.csv" by default.

```bash
python maze_solver.py --maze-file mazes/full_maze.csv
```

## How to run tests

The tests/ folder contains all the unit and integration tests for this project.
To run the tests, please run the command below in the project directory.

```bash
python -m unittest discover -v
```