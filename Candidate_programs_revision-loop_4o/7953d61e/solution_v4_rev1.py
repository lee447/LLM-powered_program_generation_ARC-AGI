from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = len(grid[0])
    result = [[0] * (2 * m) for _ in range(2 * n)]
    for i in range(n):
        for j in range(m):
            result[i][j] = grid[i][j]
            result[i][j + m] = grid[i][m - 1 - j]
            result[i + n][j] = grid[n - 1 - i][j]
            result[i + n][j + m] = grid[n - 1 - i][m - 1 - j]
    return result