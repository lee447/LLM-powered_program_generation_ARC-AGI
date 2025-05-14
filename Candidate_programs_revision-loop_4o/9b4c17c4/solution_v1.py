from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    result = [row[:] for row in grid]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                if r > 0 and grid[r-1][c] == 8:
                    result[r-1][c] = 2
                if r < rows - 1 and grid[r+1][c] == 8:
                    result[r+1][c] = 2
                if c > 0 and grid[r][c-1] == 8:
                    result[r][c-1] = 2
                if c < cols - 1 and grid[r][c+1] == 8:
                    result[r][c+1] = 2

    return result