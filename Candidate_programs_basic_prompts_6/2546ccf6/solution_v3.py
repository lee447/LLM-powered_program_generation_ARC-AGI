from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    sep_rows = [i for i in range(H) if grid[i][0] != 0 and all(grid[i][j] == grid[i][0] for j in range(W))]
    sep_cols = [j for j in range(W) if grid[0][j] != 0 and all(grid[i][j] == grid[0][j] for i in range(H))]
    sep_color = grid[sep_rows[0]][0]
    row_intervals = []
    prev = 0
    for r in sep_rows:
        if prev <= r-1:
            row_intervals.append((prev, r-1))
        prev = r+1
    if prev <= H-1:
        row_intervals.append((prev, H-1))
    col_intervals = []
    prev = 0
    for c in sep_cols:
        if prev <= c-1:
            col_intervals.append((prev, c-1))
        prev = c+1
    if prev <= W-1:
        col_intervals.append((prev, W-1))
    colored_block = None
    for j, (c0, c1) in enumerate(col_intervals):
        found = False
        for i in range(H):
            for c in range(c0, c1+1):
                v = grid[i][c]
                if v != 0 and v != sep_color:
                    found = True
                    break
            if found:
                break
        if found:
            colored_block = j
            break
    if colored_block is None or colored_block+1 >= len(col_intervals):
        return grid
    target = colored_block + 1
    w0 = col_intervals[colored_block][1] - col_intervals[colored_block][0] + 1
    grid_out = [row[:] for row in grid]
    for (r0, r1) in row_intervals:
        for i in range(r0, r1+1):
            for dx in range(w0):
                x = col_intervals[colored_block][0] + dx
                v = grid[i][x]
                if v != 0 and v != sep_color:
                    mirror_dx = w0 - 1 - dx
                    tx = col_intervals[target][0] + mirror_dx
                    grid_out[i][tx] = v
    return grid_out