from typing import List
import numpy as np

def solve(grid: List[List[int]]) -> List[List[int]]:
    grid = np.array(grid)
    rows, cols = grid.shape
    result = np.zeros_like(grid)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                if r + 1 < rows and grid[r + 1][c] == 0:
                    result[r + 1][c] = 2
                if c + 1 < cols and grid[r][c + 1] == 0:
                    result[r][c + 1] = 2
                if r - 1 >= 0 and grid[r - 1][c] == 0:
                    result[r - 1][c] = 2
                if c - 1 >= 0 and grid[r][c - 1] == 0:
                    result[r][c - 1] = 2

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 3:
                if r + 1 < rows and grid[r + 1][c] == 0:
                    result[r + 1][c] = 3
                if c + 1 < cols and grid[r][c + 1] == 0:
                    result[r][c + 1] = 3
                if r - 1 >= 0 and grid[r - 1][c] == 0:
                    result[r - 1][c] = 3
                if c - 1 >= 0 and grid[r][c - 1] == 0:
                    result[r][c - 1] = 3

    for r in range(rows):
        for c in range(cols):
            if result[r][c] == 0:
                result[r][c] = grid[r][c]

    return result.tolist()