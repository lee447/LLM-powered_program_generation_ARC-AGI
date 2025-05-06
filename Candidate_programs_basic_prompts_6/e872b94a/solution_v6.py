from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    d = sum(1 for i in range(min(h, w)) if grid[i][i] == 5)
    return [[0] for _ in range(d + (1 if w > h else 0))]