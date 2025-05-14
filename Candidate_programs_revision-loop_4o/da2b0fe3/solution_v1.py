from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                if r + 1 < rows and grid[r + 1][c] == 0:
                    for cc in range(cols):
                        grid[r + 1][cc] = 3
                if c + 1 < cols and grid[r][c + 1] == 0:
                    for rr in range(rows):
                        grid[rr][c + 1] = 3
    return grid