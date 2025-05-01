def solve(grid):
    R, C = len(grid), len(grid[0])
    DIV, PLACE = 4, 1
    full_rows = [i for i in range(R) if all(grid[i][j] == DIV for j in range(C))]
    full_cols = [j for j in range(C) if all(grid[i][j] == DIV for i in range(R))]
    row_segs = []
    prev = 0
    for r in sorted(full_rows):
        if prev <= r - 1:
            row_segs.append((prev, r - 1))
        prev = r + 1
    if prev <= R - 1:
        row_segs.append((prev, R - 1))
    col_segs = []
    prev = 0
    for c in sorted(full_cols):
        if prev <= c - 1:
            col_segs.append((prev, c - 1))
        prev = c + 1
    if prev <= C - 1:
        col_segs.append((prev, C - 1))
    x_val = None
    for i in range(R):
        for j in range(C):
            v = grid[i][j]
            if v not in (0, PLACE, DIV):
                x_val, i0, j0 = v, i, j
                break
        if x_val is not None:
            break
    for zi, (rs, re) in enumerate(row_segs):
        if rs <= i0 <= re:
            break
    for zj, (cs, ce) in enumerate(col_segs):
        if cs <= j0 <= ce:
            break
    zr, zr_end = row_segs[zi]
    zc, zc_end = col_segs[zj]
    offsets = [(i - zr, j - zc) for i in range(zr, zr_end + 1) for j in range(zc, zc_end + 1) if grid[i][j] == x_val]
    for zi2, (rs, re) in enumerate(row_segs):
        for zj2, (cs, ce) in enumerate(col_segs):
            if zi2 == zi and zj2 == zj:
                continue
            for dr, dc in offsets:
                i2, j2 = rs + dr, cs + dc
                if rs <= i2 <= re and cs <= j2 <= ce and grid[i2][j2] == PLACE:
                    grid[i2][j2] = x_val
    return grid