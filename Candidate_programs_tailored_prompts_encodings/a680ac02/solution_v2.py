def solve(grid):
    h, w = len(grid), len(grid[0])
    rings = []
    for r in range(h - 3):
        for c in range(w - 3):
            v = grid[r][c]
            if v == 0: continue
            ok = True
            for di in range(4):
                for dj in range(4):
                    val = grid[r+di][c+dj]
                    if di in (0,3) or dj in (0,3):
                        if val != v: ok = False
                    else:
                        if val != 0: ok = False
                    if not ok: break
                if not ok: break
            if ok:
                rings.append((r, c, v))
    if not rings:
        return [[0]]
    rows = [r for r, c, v in rings]
    cols_ = [c for r, c, v in rings]
    row_range = max(rows) - min(rows)
    col_range = max(cols_) - min(cols_)
    rings.sort(key=lambda x: (x[1], x[0]))
    k = len(rings)
    if col_range >= row_range:
        out_h, out_w = 4, 4 * k
        out = [[0] * out_w for _ in range(out_h)]
        for i, (r, c, v) in enumerate(rings):
            base = 4 * i
            for di in range(4):
                for dj in range(4):
                    out[di][base+dj] = grid[r+di][c+dj]
    else:
        out_h, out_w = 4 * k, 4
        out = [[0] * out_w for _ in range(out_h)]
        for i, (r, c, v) in enumerate(rings):
            base = 4 * i
            for di in range(4):
                for dj in range(4):
                    out[base+di][dj] = grid[r+di][c+dj]
    return out