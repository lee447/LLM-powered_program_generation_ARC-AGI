from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    r, c = len(grid), len(grid[0])
    zeros = [(i, j) for i in range(r) for j in range(c) if grid[i][j] == 0]
    color = next(grid[i][j] for i in range(r) for j in range(c) if grid[i][j] != 0)
    out = [[0] * (c * c) for _ in range(r * r)]
    for bi, bj in zeros:
        for di, dj in zeros:
            out[bi * r + di][bj * c + dj] = color
    return out