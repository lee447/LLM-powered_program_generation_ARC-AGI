from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    zero_rows = [i for i in range(h) if any(grid[i][j] == 0 for j in range(w))]
    r1, r2 = zero_rows[0], zero_rows[1]
    cols1 = [j for j in range(w) if grid[r1][j] == 0]
    cols2 = [j for j in range(w) if grid[r2][j] == 0]
    avg1 = sum(cols1) / len(cols1)
    avg2 = sum(cols2) / len(cols2)
    slope = 1 if avg2 >= avg1 else -1
    initial = min(cols1) if slope > 0 else max(cols1)
    for i in zero_rows:
        ideal = initial + slope * (i - r1)
        if 0 <= ideal < w and grid[i][ideal] == 0:
            out[i][ideal] = 8
    return out