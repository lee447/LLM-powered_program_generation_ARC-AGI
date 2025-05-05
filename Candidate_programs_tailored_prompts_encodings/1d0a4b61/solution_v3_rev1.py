import numpy as np
from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    def has_zero(row): return any(x==0 for x in row)
    non_zero = [i for i in range(n) if not has_zero(grid[i])]
    if not non_zero: return res
    d = None
    for i in range(1, n):
        if not has_zero(grid[i]) and grid[i] == grid[0]:
            d = i
            break
    if d is None: d = n
    template = {}
    for rem in range(d):
        for r in non_zero:
            if r % d == rem:
                template[rem] = grid[r]
                break
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                res[i][j] = template[i % d][j]
    return res