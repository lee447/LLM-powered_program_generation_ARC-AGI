from typing import List
import numpy as np

def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    result = np.zeros((n, m), dtype=int)
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0:
                color = grid[i][j]
                if i + 1 < n and grid[i + 1][j] == color:
                    k = i
                    while k < n and grid[k][j] == color:
                        result[k][j] = color
                        k += 1
                if j + 1 < m and grid[i][j + 1] == color:
                    k = j
                    while k < m and grid[i][k] == color:
                        result[i][k] = color
                        k += 1
    return result.tolist()