from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0]) if grid else 0
    n = len({v for row in grid for v in row})
    return [[grid[i % R][j % C] for j in range(C * n)] for i in range(R * n)]