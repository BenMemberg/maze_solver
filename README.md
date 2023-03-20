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

Running with a file
```bash
python solver.py --maze-file mazes/full_maze.csv
```

Running with a generated maze
```bash
python solver.py --maze-size 30x20
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

## Reflection/Analysis

### Analysis Story 1
"At this point, you may have created a general-purpose solver. If not, try to identify some types of
mazes that your algorithm would not solve correctly."

I did end up implementing a general-purpose maze solver. That being said, my maze solver could not solve a maze where the exit wasn't in the bottom row. This is because every sample maze had their exit in the last row, so I made that a specification for determining if the agent was at an exit. It would also only ever navigate to the first exit found (if there is more than one valid exit).

### Analysis Story 2
"If you kept things simple, it is likely that your algorithm may not be as efficient as possible.
Describe the solution’s complexity and approaches that could be used to optimize it further."

My algorithm has no real heuristic and it has a static timeout value, so for an M x N matrix with a given timout C, the time complexity is either O(C) or O(M*N). This complexity can be improved by adding heuristics, like for proximity to the exit location. Another way to improve the algorithm would be to geive the agent a global view of the maze so it can search all routes at the same time (this would remove the need for the timeout as the agent could determine when all spaces have been searched).

### Analysis Story 3
"Moving robots isn’t as simple as moving a 1x1 pixel through a maze. Instead, we must plan a
path while avoiding obstacles using a collision model. We can approximate this by plotting a
path for a 1x3 “ship” through a maze. In addition to moving “backward” and “forward” the ship
can also rotate around its center of gravity provided it is in the center of a 3x3

Do not code a solution, but instead describe an approach for decomposing this problem into
incremental stories as done for the maze problem above."

Incremental Solution Stories:
1) Find maze entry with a 1x3 space to enter.
2) Walk ship down straight hallway.
3) Move ship left and right.
4) Ship can move backwards if it gets stuck.
4) Ship can identify when it is in the middle of a 3x3 room (and thus rotate).
5) Add ability to rotate ship (and stay in that rotation while moving).
6) Ship can identify exit.