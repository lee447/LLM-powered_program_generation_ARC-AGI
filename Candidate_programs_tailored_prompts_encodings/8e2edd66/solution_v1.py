from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    N = len(grid)
    color = next(grid[i][j] for i in range(N) for j in range(N) if grid[i][j] != 0)
    zeros = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == 0]
    M = N * N
    out = [[0] * M for _ in range(M)]
    for bi, bj in zeros:
        for li, lj in zeros:
            out[bi * N + li][bj * N + lj] = color
    return out