from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    color = next(grid[i][j] for i in range(n) for j in range(n) if grid[i][j] != 0)
    P = [[grid[u][v] == 0 for v in range(n)] for u in range(n)]
    out = [[0] * (n * n) for _ in range(n * n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                bi, bj = i * n, j * n
                for u in range(n):
                    for v in range(n):
                        if P[u][v]:
                            out[bi + u][bj + v] = color
    return out