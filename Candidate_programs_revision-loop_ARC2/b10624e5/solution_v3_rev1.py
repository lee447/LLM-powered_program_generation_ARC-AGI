from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    res = [row[:] for row in grid]
    axis = next(j for j in range(w) if all(grid[i][j] == 1 for i in range(h)))
    bg = grid[0][0]
    for i in range(h):
        for j in range(axis):
            v = grid[i][j]
            if v != bg:
                nj = 2 * axis - j
                if 0 <= nj < w:
                    res[i][nj] = v
    return res