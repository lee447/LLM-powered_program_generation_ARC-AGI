from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for r in range(h - 2):
        for c in range(w - 2):
            window = [grid[r+i][c+j] for i in range(3) for j in range(3)]
            if 4 in window:
                continue
            if grid[r+1][c] == 8 and grid[r+1][c+1] == 1 and out[r+1][c+2] == 0:
                out[r+1][c+2] = 4
            if grid[r+1][c+1] == 1 and grid[r+1][c+2] == 8 and out[r+1][c] == 0:
                out[r+1][c] = 4
            if grid[r][c+1] == 8 and grid[r+1][c+1] == 1 and out[r+2][c+1] == 0:
                out[r+2][c+1] = 4
            if grid[r+1][c+1] == 1 and grid[r+2][c+1] == 8 and out[r][c+1] == 0:
                out[r][c+1] = 4
    return out