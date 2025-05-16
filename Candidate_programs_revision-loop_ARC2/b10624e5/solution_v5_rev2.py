from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    res = [row[:] for row in grid]
    axis = next(j for j in range(w) if all(grid[i][j] == 1 for i in range(h)))
    bg = grid[0][0]
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v != bg and v != 1:
                mj = 2 * axis - j
                if 0 <= mj < w:
                    if j < axis:
                        res[i][mj] = v
                    elif res[i][mj] == bg:
                        res[i][mj] = v
    return res