from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    sep_color = next(row[0] for row in grid if len(set(row)) == 1)
    sep_rows = [i for i, row in enumerate(grid) if all(v == sep_color for v in row)]
    sep_cols = [j for j in range(cols) if all(grid[i][j] == sep_color for i in range(rows))]
    sep_rows.sort()
    sep_cols.sort()
    row_bounds = []
    prev = -1
    for sr in sep_rows:
        if sr - prev > 1:
            row_bounds.append((prev + 1, sr))
        prev = sr
    if rows - 1 - prev >= 0:
        row_bounds.append((prev + 1, rows))
    col_bounds = []
    prev = -1
    for sc in sep_cols:
        if sc - prev > 1:
            col_bounds.append((prev + 1, sc))
        prev = sc
    if cols - 1 - prev >= 0:
        col_bounds.append((prev + 1, cols))
    result = []
    for rs, re in row_bounds:
        row = []
        for cs, ce in col_bounds:
            row.append(grid[rs][cs])
        result.append(row)
    return result