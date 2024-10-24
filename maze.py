import numpy as np
from PIL import Image
import random


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = np.zeros((height, width), dtype=int)
        self.solution = []

    def fill_board(self):
        "Rellena el tablero completamente con paredes."""
        self.maze = np.ones((self.height, self.width), dtype=int)

    def carve_path(self, current):
        """Create a path from the current cell using backtracking."""
        x, y = current
        self.maze[x, y] = 0  # Set the current cell as path

        # Mix the addresses to make the random walk
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < self.height and 0 < ny < self.width and self.maze[nx, ny] == 1:
                # If the adjacent cell is empty, create a path
                self.maze[x + dx // 2, y + dy // 2] = 0  # Remove the wall between
                self.carve_path((nx, ny))  # Recursion

    def generate_maze(self):
        """Generates the maze completely filled except for the path."""
        # Initialize the maze with walls
        self.fill_board()

        # Start carving the maze from the starting cell
        self.carve_path((1, 1))

        return self.maze


    def fill_board(self):
        """Fill the board completely with walls."""
        self.maze = np.ones((self.height, self.width), dtype=int)

    def carve_path(self, current):
        """Create a path from the current cell using backtracking."""
        x, y = current
        self.maze[x, y] = 0  # Set the current cell as path

        # Mix the addresses to make the random walk
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < self.height and 0 < ny < self.width and self.maze[nx, ny] == 1:
                # If the adjacent cell is empty, create a path
                self.maze[x + dx // 2, y + dy // 2] = 0  # Remove the wall between
                self.carve_path((nx, ny))  # Recursión

    def generate_maze(self):
        """Generates the maze completely filled except for the path."""
        # Initialize the maze with walls
        self.fill_board()

        # Start carving the maze from the starting cell
        self.carve_path((1, 1))

        return self.maze

    def solve_maze(self, start=(1, 1), end=None):
        if end is None:
            end = (self.height - 2, self.width - 2)

        # Depth Search (DFS) Algorithm
        stack = [start]
        visited = set()
        parent = {start: None}

        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)

            if current == end:
                break

            x, y = current
            neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            for neighbor in neighbors:
                nx, ny = neighbor
                if 0 <= nx < self.height and 0 <= ny < self.width and self.maze[nx, ny] == 0 and neighbor not in visited:
                    stack.append(neighbor)
                    parent[neighbor] = current

        # Rebuild the road
        current = end
        while current:
            self.solution.append(current)
            current = parent[current]

        self.solution.reverse()
        return self.solution

    def export_to_image(self, filename):
        img = Image.new('RGB', (self.width * 10, self.height * 10), color='white')
        pixels = img.load()

        for x in range(self.height):
            for y in range(self.width):
                if self.maze[x, y] == 1:
                    color = (0, 0, 0)  # Pared
                else:
                    color = (255, 255, 255)  # Camino
                for i in range(10):
                    for j in range(10):
                        pixels[y * 10 + j, x * 10 + i] = color

        # Dibujar la solución
        for (x, y) in self.solution:
            for i in range(10):
                for j in range(10):
                    pixels[y * 10 + j, x * 10 + i] = (255, 0, 0)  # Solución en rojo

        img.save(filename)


# Example of use
if __name__ == "__main__":
    maze = Maze(61, 61)  # Odd dimensions for maze generation
    maze.generate_maze()
    maze.solve_maze()
    maze.export_to_image('maze.png')
    print("Labyrinth and its solution exported to 'maze.png'.")
