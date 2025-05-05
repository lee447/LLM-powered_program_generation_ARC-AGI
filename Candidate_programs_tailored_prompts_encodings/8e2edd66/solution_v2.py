from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    color = next(val for row in grid for val in row if val != 0)
    mask = [[grid[i][j] == 0 for j in range(n)] for i in range(n)]
    N = n * n
    out = [[0] * N for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if mask[i][j]:
                for u in range(n):
                    for v in range(n):
                        if mask[u][v]:
                            out[i*n + u][j*n + v] = color
    return out