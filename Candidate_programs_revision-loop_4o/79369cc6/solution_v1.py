from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 6:
                if c + 1 < cols and grid[r][c + 1] == 6:
                    if c + 2 < cols and grid[r][c + 2] == 6:
                        grid[r][c + 1] = 4
                        grid[r][c + 2] = 4
                if r + 1 < rows and grid[r + 1][c] == 6:
                    if r + 2 < rows and grid[r + 2][c] == 6:
                        grid[r + 1][c] = 4
                        grid[r + 2][c] = 4
    return grid