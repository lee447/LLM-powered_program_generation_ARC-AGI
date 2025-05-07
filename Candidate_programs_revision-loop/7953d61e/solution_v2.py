from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    def rot90(g):
        m = len(g)
        return [[g[m-1-j][i] for j in range(m)] for i in range(m)]
    r0 = grid
    r90 = rot90(r0)
    r180 = rot90(r90)
    r270 = rot90(r180)
    out = [[0]*(2*n) for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            out[i][j] = r0[i][j]
            out[i][j+n] = r270[i][j]
            out[i+n][j] = r180[i][j]
            out[i+n][j+n] = r90[i][j]
    return out