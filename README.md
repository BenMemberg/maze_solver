# Maze Solver

This project contains the code to solve a given maze file (either a sample or a custom maze).

## How to use the maze solver

The main execution file for the project is solver.py. It takes two optional
arguments:

- `--maze-file <PATH_TO_FILE>` or `-m <PATH_TO_FILE>`: The maze file should be
    the path from the project folder to the target maze file to solve. If the 
    maze file argument is not provided, the solver will use the file
    "mazes/full_maze.csv" by default.
- `--timeout <INT>` or `-t <INT>`: The timeout should be an integer
    representing the number of steps the solver can explore before it times
    out. Defaults to 1000 if not provided (1000 should be sufficient for most
    simple mazes but it should be increased for mazes more complex mazes).

```bash
python maze_solver.py --maze-file mazes/full_maze.csv
```

### Custom Maze Files

This project should act as a generalized maze solver, so it is also compatible
with custom maze files.


A custom maze file must be:
- In binary csv format (a csv of all ones and zeros), where 1s represent walls
  and 0s represent open spaces.
    
    Here is the content of a 3x4 example maze file:
    ```
    1,1,0,1
    1,0,0,1
    1,0,1,1
    ```
- Consistent dimensions for each row/column. The file must represent an `m x n`
  matrix. This project is not set up to handle mazes of a different shape.
- (optional) Placed in the projects folder, preferably in the mazes/ folder.
  Otherwise the maze-file path will need to be an absolute path.

Note: If the custom maze is much more complex than a 10x10, consider increasing the maze solver timeout arg.


## How to Run Tests

The tests/ folder contains all the unit and integration tests for this project.
To run the tests, please run one of the commands below in the project directory.

```bash
# Run all tests
python -m unittest discover -v

# Run a specific test class
python -m unittest tests.test_maze_agent.TestMazeAgent -v

# Run a specific test
python -m unittest tests.test_user_story_integration.TestUserStories.test_full_maze
```