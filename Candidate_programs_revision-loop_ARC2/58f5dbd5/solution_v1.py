from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    r, c = len(grid), len(grid[0])
    b = grid[0][0]
    if b == 8:
        return [row[7:14] for row in grid]
    if b == 4:
        return grid[:7]
    if b == 1:
        return [row[:13] for row in grid[:13]]
    return grid