from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    rccw = [[grid[j][n-1-i] for j in range(n)] for i in range(n)]
    rcw = [[grid[n-1-j][i] for j in range(n)] for i in range(n)]
    r180 = [row[::-1] for row in grid[::-1]]
    out = [[0]*(2*n) for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            out[i][j] = grid[i][j]
            out[i][j+n] = rccw[i][j]
            out[i+n][j] = r180[i][j]
            out[i+n][j+n] = rcw[i][j]
    return out