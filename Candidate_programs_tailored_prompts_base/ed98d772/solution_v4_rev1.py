from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    def rot90(g):
        return [[g[n-1-j][i] for j in range(n)] for i in range(n)]
    g90 = rot90(grid)
    g180 = rot90(g90)
    g270 = rot90(g180)
    out = [[0]*(2*n) for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            out[i][j] = grid[i][j]
            out[i][j+n] = g270[i][j]
            out[i+n][j] = g180[i][j]
            out[i+n][j+n] = g90[i][j]
    return out