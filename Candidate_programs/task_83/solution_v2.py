import numpy as np
from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    output = [row.copy() for row in grid]
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        output[r][cols // 2] = 3

    return output