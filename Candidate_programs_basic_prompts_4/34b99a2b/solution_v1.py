from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = len(grid[0])
    d = next(c for c in range(m) if all(grid[r][c] == 4 for r in range(n)))
    w = min(d, m - d - 1)
    res = [[0] * w for _ in range(n)]
    for i in range(n):
        for j in range(w):
            if (grid[i][j] != 0) ^ (grid[i][d + 1 + j] != 0):
                res[i][j] = 2
    return res