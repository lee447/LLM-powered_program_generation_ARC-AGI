from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    if h == 0:
        return []
    w = len(grid[0])
    out = [[0] * (2 * w) for _ in range(2 * h)]
    for i, row in enumerate(grid):
        pattern = row[::-1] + row[:]
        out[h - 1 - i] = pattern
        out[h + i] = pattern
    return out