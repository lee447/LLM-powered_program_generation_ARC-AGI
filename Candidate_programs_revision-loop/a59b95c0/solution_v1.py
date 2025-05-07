from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    rows = len(grid)
    cols = len(grid[0])
    k = len({v for row in grid for v in row})
    return [[grid[i % rows][j % cols] for j in range(cols * k)] for i in range(rows * k)]