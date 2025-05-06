from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    out = [[0] * (2 * w) for _ in range(2 * h)]
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            ii = 2 * i
            jj = 2 * j
            out[ii][jj] = v
            out[ii][jj + 1] = v
            out[ii + 1][jj] = v
            out[ii + 1][jj + 1] = v
    return out