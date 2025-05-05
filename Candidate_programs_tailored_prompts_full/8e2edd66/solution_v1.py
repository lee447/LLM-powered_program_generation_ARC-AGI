from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    mask = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 0]
    color = next(grid[i][j] for i in range(n) for j in range(n) if grid[i][j] != 0)
    N = n * n
    out = [[0] * N for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                bi, bj = i * n, j * n
                for mi, mj in mask:
                    out[bi + mi][bj + mj] = color
    return out