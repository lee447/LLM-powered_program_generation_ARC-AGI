def solve(grid):
    h = len(grid)
    w = len(grid[0])
    occ = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v:
                occ.setdefault(v, []).append((r, c))
    out = [[0]*w for _ in range(h)]
    for v, pts in occ.items():
        if len(pts) == 1:
            r, c = pts[0]
            out[r][c] = v
        else:
            cols = sorted({c for _, c in pts})
            pivot = cols[len(cols)//2]
            rows = [r for r, _ in pts]
            for r in range(min(rows), max(rows)+1):
                out[r][pivot] = v
    return out