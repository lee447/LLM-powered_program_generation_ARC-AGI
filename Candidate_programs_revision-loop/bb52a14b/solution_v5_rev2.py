from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if grid[i][j] in (1, 8):
                if 0 <= j-1 and grid[i][j-1] == 0 and 0 <= j+1 < w and grid[i][j+1] == 0:
                    out[i][j-1] = 4
                    out[i][j+1] = 4
    for i in range(1, h-1):
        for j in range(1, w-1):
            if grid[i][j] == 8:
                if any(grid[i+di][j+dj] != 0 for di, dj in [(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)]):
                    for di, dj in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                        ni, nj = i+di, j+dj
                        if 0 <= ni < h and 0 <= nj < w and out[ni][nj] == 0:
                            p = 8 if (di, dj) == (0, 0) else 4 if di == 0 or dj == 0 else 1
                            out[ni][nj] = p
    return out