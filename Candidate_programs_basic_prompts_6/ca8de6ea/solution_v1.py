from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    mid = n // 2
    return [
        [grid[0][0], grid[1][1], grid[0][n-1]],
        [grid[n-2][1], grid[mid][mid], grid[1][n-2]],
        [grid[n-1][0], grid[n-2][n-2], grid[n-1][n-1]],
    ]