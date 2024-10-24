# Maze Generator and Solver

This project is a Python maze generator that uses a **backtracking** algorithm to create fully filled mazes, and then solves the maze using depth-first search. The generated mazes can be exported as images for easy visualization.

## Contents

- `maze.py`: Contains the `Maze` class that implements the generation, solving, and image export of the maze.
- `maze.png`: Image of the generated maze and its solution (automatically generated).

## Requirements

- Python 3.x
- Numpy
- Pillow


## Running the Script

- Windows:
  Ensure that bash is available. This can be done through Git Bash or Windows Subsystem for Linux (WSL). To run the script, use the following command:

```bash
bash setup_env.sh
```

- Linux and macOS:
  Before running the script, ensure it has execution permissions. You can set this by running:

```bash
chmod +x setup_env.sh
```

- Additional Notes
  If you encounter any issues with the script or have questions about the setup process, feel free to ask for assistance.


## How to Use

1. Clone the repository https://github.com/ProWilliam/Maze_generator.git

2. Or download the maze.py file.

2. Ensure you have Python and the dependencies installed.

3. Run the script as follows:

```bash
python maze.py
```

## Maze Visualization

The generated mazes are displayed as images, with the maze structure represented in black and the paths in white. The solution path is highlighted in red. Below are some examples of what the mazes look like:

### Example 1
![Example Maze 1](https://raw.githubusercontent.com/ProWilliam/Maze_generator/refs/heads/main/maze_1.png)

### Example 2
![Example Maze 2](https://raw.githubusercontent.com/ProWilliam/Maze_generator/refs/heads/main/maze_2.png)

### Example 3
![Example Maze 3](https://raw.githubusercontent.com/ProWilliam/Maze_generator/refs/heads/main/maze_3.png)

### How to View
After running the script, the maze and its solution will be saved as `maze.png` in the project directory. You can open this image with any image viewer to see the maze layout and the solution path.
