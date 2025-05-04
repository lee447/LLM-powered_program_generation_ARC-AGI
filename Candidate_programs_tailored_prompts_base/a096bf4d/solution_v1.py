def solve(grid):
    h, w = len(grid), len(grid[0])
    black = 0
    sep_rows = [i for i in range(h) if all(grid[i][j] == black for j in range(w))]
    sep_cols = [j for j in range(w) if all(grid[i][j] == black for i in range(h))]
    row_segments = []
    for i in range(len(sep_rows) - 1):
        a, b = sep_rows[i] + 1, sep_rows[i + 1]
        if a < b:
            row_segments.append((a, b))
    col_segments = []
    for i in range(len(sep_cols) - 1):
        a, b = sep_cols[i] + 1, sep_cols[i + 1]
        if a < b:
            col_segments.append((a, b))
    blocks = []
    for br, (r_start, r_end) in enumerate(row_segments):
        for bc, (c_start, c_end) in enumerate(col_segments):
            ih = r_end - r_start
            iw = c_end - c_start
            r0 = r_start + ih // 2 - 1
            c0 = c_start + iw // 2 - 1
            coords = [(r0 + i, c0 + j) for i in (0, 1) for j in (0, 1)]
            vals = [grid[r][c] for r, c in coords]
            cnt = {}
            for v in vals:
                cnt[v] = cnt.get(v, 0) + 1
            cluster_color = max(cnt.items(), key=lambda x: x[1])[0]
            for (r, c), v in zip(coords, vals):
                if v != cluster_color:
                    blocks.append((br, r, c, v))
                    break
    modes = {}
    for br in range(len(row_segments)):
        cols = [b[3] for b in blocks if b[0] == br]
        cnt = {}
        for c in cols:
            cnt[c] = cnt.get(c, 0) + 1
        modes[br] = max(cnt.items(), key=lambda x: x[1])[0]
    out = [row[:] for row in grid]
    for br, r, c, _ in blocks:
        out[r][c] = modes[br]
    return out