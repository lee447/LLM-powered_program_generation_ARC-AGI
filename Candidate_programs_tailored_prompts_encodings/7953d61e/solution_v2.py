from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    ccw = [[grid[j][n-1-i] for j in range(n)] for i in range(n)]
    rot180 = [[grid[n-1-i][n-1-j] for j in range(n)] for i in range(n)]
    cw = [[grid[n-1-j][i] for j in range(n)] for i in range(n)]
    out = [[0]*(2*n) for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            v = grid[i][j]
            out[i][j] = v
            out[i][j+n] = ccw[i][j]
            out[i+n][j] = rot180[i][j]
            out[i+n][j+n] = cw[i][j]
    return out