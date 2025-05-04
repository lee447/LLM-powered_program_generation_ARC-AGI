from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    cw = [[grid[n-1-j][i] for j in range(n)] for i in range(m)]
    ccw = [[grid[j][m-1-i] for j in range(n)] for i in range(m)]
    rot180 = [[grid[n-1-i][m-1-j] for j in range(m)] for i in range(n)]
    res = [[0]*(m*2) for _ in range(n*2)]
    for i in range(n):
        for j in range(m):
            res[i][j] = grid[i][j]
            res[i][j+m] = ccw[i][j]
            res[i+n][j] = rot180[i][j]
            res[i+n][j+m] = cw[i][j]
    return res