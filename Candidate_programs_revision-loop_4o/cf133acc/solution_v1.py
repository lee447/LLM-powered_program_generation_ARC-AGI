from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    output = [[0] * cols for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                color = grid[r][c]
                if r > 0 and grid[r-1][c] == 0:
                    output[r-1][c] = color
                if r < rows - 1 and grid[r+1][c] == 0:
                    output[r+1][c] = color
                if c > 0 and grid[r][c-1] == 0:
                    output[r][c-1] = color
                if c < cols - 1 and grid[r][c+1] == 0:
                    output[r][c+1] = color
                output[r][c] = color
    
    return output