from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = len(grid[0])
    new_size = n + m - 1
    result = [[0] * new_size for _ in range(new_size)]
    
    for i in range(n):
        for j in range(m):
            result[i][j] = grid[i][j]
            result[i + j][j] = grid[i][j]
            result[i][j + i] = grid[i][j]
            result[i + j][j + i] = grid[i][j]
    
    return result