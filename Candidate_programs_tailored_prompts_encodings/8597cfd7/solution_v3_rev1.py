from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    sep = next(i for i, row in enumerate(grid) if all(c == 5 for c in row))
    red_above = sum(1 for r in range(sep) for c in grid[r] if c == 2)
    red_below = sum(1 for r in range(sep + 1, h) for c in grid[r] if c == 2)
    y_above = sum(1 for r in range(sep) for c in grid[r] if c == 4)
    y_below = sum(1 for r in range(sep + 1, h) for c in grid[r] if c == 4)
    winner = 2 if (red_below - red_above) >= (y_below - y_above) else 4
    return [[winner, winner], [winner, winner]]