from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = len(grid[0])
    output = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                output[i][j] = 2
            else:
                output[i][j] = 0
    
    return output