def solve(grid):
    h, w = len(grid), len(grid[0])
    sep_rows = [i for i in range(h) if all(grid[i][j] == 4 for j in range(w))]
    sep_cols = [j for j in range(w) if all(grid[i][j] == 4 for i in range(h))]
    sep_rows.sort()
    sep_cols.sort()
    row_bounds = []
    prev = 0
    for r in sep_rows:
        if r > prev:
            row_bounds.append((prev, r - prev))
        prev = r + 1
    if prev < h:
        row_bounds.append((prev, h - prev))
    col_bounds = []
    prev = 0
    for c in sep_cols:
        if c > prev:
            col_bounds.append((prev, c - prev))
        prev = c + 1
    if prev < w:
        col_bounds.append((prev, w - prev))
    motif = None
    mb_r = mb_c = None
    for br, bh in row_bounds:
        for bc, bw in col_bounds:
            coords = []
            color = None
            for r in range(br, br + bh):
                for c in range(bc, bc + bw):
                    v = grid[r][c]
                    if v not in (0, 1, 4):
                        coords.append((r - br, c - bc))
                        color = v
            if coords:
                motif = (color, coords)
                mb_r, mb_c = br, bc
                break
        if motif:
            break
    if motif is None:
        return grid
    color, rel = motif
    inner_rows = []
    for i in range(len(sep_rows) - 1):
        start = sep_rows[i] + 1
        height = sep_rows[i+1] - sep_rows[i] - 1
        if height > 0:
            inner_rows.append((start, height))
    inner_cols = []
    for j in range(len(sep_cols) - 1):
        start = sep_cols[j] + 1
        width = sep_cols[j+1] - sep_cols[j] - 1
        if width > 0:
            inner_cols.append((start, width))
    out = [row[:] for row in grid]
    for br, bh in inner_rows:
        for bc, bw in inner_cols:
            if br == mb_r and bc == mb_c:
                continue
            for dr, dc in rel:
                r, c = br + dr, bc + dc
                if 0 <= r < h and 0 <= c < w and grid[r][c] in (0, 1):
                    out[r][c] = color
    return out