from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = len(grid[0])
    result = [row[:] for row in grid]
    
    for i in range(n):
        for j in range(m):
            if i < n // 2 and j < m // 2:
                result[i][j] = grid[i][j]
            elif i < n // 2 and j >= m // 2:
                result[i][j] = grid[i][j - m // 2]
            elif i >= n // 2 and j < m // 2:
                result[i][j] = grid[i - n // 2][j]
            else:
                result[i][j] = grid[i - n // 2][j - m // 2]
    
    return result