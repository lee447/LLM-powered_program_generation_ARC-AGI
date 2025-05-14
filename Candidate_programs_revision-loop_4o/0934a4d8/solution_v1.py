from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = len(grid[0])
    result = []
    for i in range(n):
        if i < n // 2:
            result.append(grid[i][m//2-2:m//2+2])
        else:
            result.append(grid[i][m//2-3:m//2+4])
    return result