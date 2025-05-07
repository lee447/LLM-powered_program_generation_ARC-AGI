from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    def rot(g: List[List[int]]) -> List[List[int]]:
        m = len(g)
        r = [[0]*m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                r[j][m-1-i] = g[i][j]
        return r
    r1 = rot(grid)
    r2 = rot(r1)
    r3 = rot(r2)
    out: List[List[int]] = []
    for i in range(n):
        out.append(grid[i] + r3[i])
    for i in range(n):
        out.append(r2[i] + r1[i])
    return out