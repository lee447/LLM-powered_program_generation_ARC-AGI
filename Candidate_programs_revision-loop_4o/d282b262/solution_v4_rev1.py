from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = len(grid[0])
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0:
                result[i][j] = grid[i][j]
    for i in range(n):
        for j in range(m):
            if result[i][j] != 0:
                for k in range(j + 1, m):
                    if result[i][k] == 0:
                        result[i][k] = result[i][j]
                        result[i][j] = 0
                        break
    return result