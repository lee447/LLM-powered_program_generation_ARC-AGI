def solve(grid):
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    color_rows = {}
    color_cols = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c:
                color_rows.setdefault(c, {}).setdefault(i, []).append(j)
                color_cols.setdefault(c, {}).setdefault(j, []).append(i)
    hshapes = []
    hor_colors = set()
    for c, rows in color_rows.items():
        for r, cols in rows.items():
            if len(cols) >= 2:
                cols_sorted = sorted(cols)
                maxg = 1
                cur = 1
                for k in range(1, len(cols_sorted)):
                    if cols_sorted[k] == cols_sorted[k-1] + 1:
                        cur += 1
                    else:
                        if cur > maxg: maxg = cur
                        cur = 1
                if cur > maxg: maxg = cur
                if maxg >= 2:
                    hshapes.append((c, r, cols_sorted))
                    hor_colors.add(c)
    if hshapes:
        baseline = max(r for _, r, _ in hshapes)
    else:
        baseline = 0
    for c, r, cols in hshapes:
        mn = min(cols)
        mx = max(cols)
        for j in range(mn, mx+1):
            if out[r][j] == 0:
                out[r][j] = c
        for j in range(mn, mx+1):
            if grid[r][j] != c:
                for i in range(0, r+1):
                    if out[i][j] == 0:
                        out[i][j] = c
    for c, cols in color_cols.items():
        if c in hor_colors: continue
        for j, rows in cols.items():
            if rows:
                mn = min(rows + [baseline])
                mx = max(rows + [baseline])
                for i in range(mn, mx+1):
                    if out[i][j] == 0:
                        out[i][j] = c
    return out