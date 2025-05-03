from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    folded = [row[::-1] + row for row in grid]
    order = list(range(h-1, -1, -1)) + list(range(h))
    return [folded[i] for i in order]