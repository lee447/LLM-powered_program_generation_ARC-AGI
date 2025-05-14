from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                if r > 0 and grid[r-1][c] == 0:
                    grid[r-1][c] = 3
                if r < rows - 1 and grid[r+1][c] == 0:
                    grid[r+1][c] = 3
                if c > 0 and grid[r][c-1] == 0:
                    grid[r][c-1] = 3
                if c < cols - 1 and grid[r][c+1] == 0:
                    grid[r][c+1] = 3
    return grid