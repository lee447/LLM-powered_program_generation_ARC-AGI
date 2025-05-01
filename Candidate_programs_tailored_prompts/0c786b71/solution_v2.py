from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    rev_rows = [row[::-1] for row in grid]
    vr = rev_rows[::-1]
    top = [r + r[::-1] for r in vr]
    return top + top[::-1]