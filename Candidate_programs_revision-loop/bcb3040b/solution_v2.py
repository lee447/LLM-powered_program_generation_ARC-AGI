from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    coords = [(i, j) for i, row in enumerate(grid) for j, v in enumerate(row) if v == 2]
    (r1, c1), (r2, c2) = coords
    dx = (r2 > r1) - (r2 < r1)
    dy = (c2 > c1) - (c2 < c1)
    steps = max(abs(r2 - r1), abs(c2 - c1))
    result = [row[:] for row in grid]
    for k in range(steps + 1):
        i = r1 + k * dx
        j = c1 + k * dy
        result[i][j] = 3 if grid[i][j] == 1 else 2
    return result