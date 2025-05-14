from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = len(grid[0])
    result = [[0] * 9 for _ in range(9)]
    
    for i in range(n):
        for j in range(m):
            result[i][j] = grid[i][j]
            result[i + 6][j + 3] = grid[i][j]
    
    return result