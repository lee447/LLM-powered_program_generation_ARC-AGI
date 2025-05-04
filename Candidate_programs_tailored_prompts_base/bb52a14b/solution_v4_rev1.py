from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 8:
                # if there's a 1 immediately to the right, propagate a mini-diagonal of 4's
                if c+1 < w and grid[r][c+1] == 1:
                    if c+2 < w and res[r][c+2] == 0:
                        res[r][c+2] = 4
                    if r+1 < h and res[r+1][c+1] == 0:
                        res[r+1][c+1] = 4
                    if r+2 < h and c+2 < w and res[r+2][c+2] == 0:
                        res[r+2][c+2] = 4
                else:
                    # otherwise fill horizontal neighbors
                    if c-1 >= 0 and res[r][c-1] == 0:
                        res[r][c-1] = 4
                    if c+1 < w and res[r][c+1] == 0:
                        res[r][c+1] = 4
    return res