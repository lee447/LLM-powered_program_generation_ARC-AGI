from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c not in (0, 8):
                if j-1 >= 0 and j+1 < w and grid[i][j-1] == c and grid[i][j+1] == c and (j-2 < 0 or grid[i][j-2] != c) and (j+2 >= w or grid[i][j+2] != c):
                    out[i][j-1] = 8
                    out[i][j]   = 8
                    out[i][j+1] = 8
                if i-1 >= 0 and i+1 < h and grid[i-1][j] == c and grid[i+1][j] == c and (i-2 < 0 or grid[i-2][j] != c) and (i+2 >= h or grid[i+2][j] != c):
                    out[i-1][j] = 8
                    out[i][j]   = 8
                    out[i+1][j] = 8
    return out