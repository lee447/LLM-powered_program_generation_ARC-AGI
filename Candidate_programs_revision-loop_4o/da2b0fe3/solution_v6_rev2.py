from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [[0] * cols for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 3:
                new_grid[r][c] = grid[r][c]
                if r > 0 and grid[r-1][c] == 3:
                    new_grid[r-1][c] = grid[r][c]
                if r < rows - 1 and grid[r+1][c] == 3:
                    new_grid[r+1][c] = grid[r][c]
                if c > 0 and grid[r][c-1] == 3:
                    new_grid[r][c-1] = grid[r][c]
                if c < cols - 1 and grid[r][c+1] == 3:
                    new_grid[r][c+1] = grid[r][c]
    
    return new_grid