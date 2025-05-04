from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    out = [[0] * (2 * n) for _ in range(2 * n)]
    for i in range(n):
        for j in range(n):
            out[i][j] = grid[i][j]
            out[i][j + n] = grid[j][n - 1 - i]
            out[i + n][j] = grid[n - 1 - i][n - 1 - j]
            out[i + n][j + n] = grid[n - 1 - j][i]
    return out