from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    shape = next(c for row in grid for c in row if c != 0)
    fill = {8:2, 5:4, 3:1}[shape]
    return [[0 if c == shape else fill for c in row] for row in grid]