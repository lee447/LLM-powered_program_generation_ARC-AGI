from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for r in range(h-1):
        for c in range(w-1):
            if grid[r][c] == 0 and grid[r][c+1] == 0 and grid[r+1][c] == 0 and grid[r+1][c+1] == 0:
                for i in range(h):
                    out[i][c] = 0
                    out[i][c+1] = 0
                for j in range(w):
                    out[r][j] = 0
                    out[r+1][j] = 0
                return out
    return out