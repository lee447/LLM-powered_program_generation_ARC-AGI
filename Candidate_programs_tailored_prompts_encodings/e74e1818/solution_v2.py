def solve(grid):
    H = len(grid)
    W = len(grid[0])
    cols = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v != 0:
                cols.setdefault(v, []).append((r, c))
    res = [[0]*W for _ in range(H)]
    for v, pts in cols.items():
        rs = [r for r, c in pts]
        minr, maxr = min(rs), max(rs)
        h = maxr - minr + 1
        if h <= 1:
            for r, c in pts:
                res[r][c] = v
            continue
        byrow = {}
        for r, c in pts:
            byrow.setdefault(r, []).append(c)
        pats = [tuple(sorted(byrow[r])) for r in range(minr, maxr+1)]
        if pats == pats[::-1]:
            for r, c in pts:
                res[r][c] = v
        else:
            for r, c in pts:
                nr = minr + (maxr - r)
                res[nr][c] = v
    return res