def solve(grid):
    greys = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 5]
    col_count = {}
    row_count = {}
    for r, c in greys:
        col_count[c] = col_count.get(c, 0) + 1
        row_count[r] = row_count.get(r, 0) + 1
    v_col = max(col_count, key=col_count.get)
    h_row = max(row_count, key=row_count.get)
    rows_v = [r for r, c in greys if c == v_col]
    cols_h = [c for r, c in greys if r == h_row]
    vr_min, vr_max = min(rows_v), max(rows_v)
    hc_min, hc_max = min(cols_h), max(cols_h)
    hole_rows = range(vr_min + 1, vr_max)
    hole_cols = range(hc_min + 1, hc_max)
    hole = {(r, c) for r in hole_rows for c in hole_cols}
    target = None
    for r, c in hole:
        v = grid[r][c]
        if v != 0 and v != 5:
            target = v
            break
    new = [row[:] for row in grid]
    if target is not None:
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v == target and (r, c) not in hole:
                    new[r][c] = 0
    return new