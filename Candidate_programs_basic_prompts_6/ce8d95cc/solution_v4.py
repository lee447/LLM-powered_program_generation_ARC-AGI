from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    new_rows: List[List[int]] = []
    prev_row = None
    for row in grid:
        if prev_row is None or row != prev_row:
            new_rows.append(row)
            prev_row = row
    cols: List[int] = []
    prev_col = None
    width = len(grid[0])
    for j in range(width):
        col = tuple(row[j] for row in new_rows)
        if prev_col is None or col != prev_col:
            cols.append(j)
            prev_col = col
    return [[row[j] for j in cols] for row in new_rows]