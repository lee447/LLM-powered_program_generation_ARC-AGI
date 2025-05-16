from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    res = [row[:] for row in grid]
    for c in {v for row in grid for v in row if v > 1}:
        cols = [j for j in range(w) if sum(grid[i][j] == c for i in range(h)) >= 2]
        if len(cols) == 2:
            col_l, col_r = sorted(cols)
            rows_l = [i for i in range(h) if grid[i][col_l] == c]
            rows_r = [i for i in range(h) if grid[i][col_r] == c]
            row_min = max(min(rows_l), min(rows_r))
            row_max = min(max(rows_l), max(rows_r))
            for i in range(row_min, row_max + 1):
                for j in range(col_l + 1, col_r):
                    if res[i][j] == 0:
                        res[i][j] = 1
    return res