from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = len(grid[0])
    new_size = n + m - 1
    result = [[0] * new_size for _ in range(new_size)]
    
    for i in range(n):
        for j in range(m):
            for k in range(n):
                result[i + k][j] = grid[k][j]
            for k in range(m):
                result[i][j + k] = grid[i][k]
    
    return result