from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = 2 * n
    out = [[0] * m for _ in range(m)]
    offs = [(0, 0), (0, n), (n, 0), (n, n)]
    for i in range(n):
        for j in range(n):
            c = grid[i][j]
            if c == 0:
                continue
            rots = [(i, j), (n-1-j, i), (n-1-i, n-1-j), (j, n-1-i)]
            for k, (r2, c2) in enumerate(rots):
                or0, oc0 = offs[k]
                out[or0 + r2][oc0 + c2] = c
    return out