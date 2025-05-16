def solve(grid):
    H = len(grid)
    W = len(grid[0])
    bounds = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v not in bounds:
                bounds[v] = [r, r, c, c]
            else:
                b = bounds[v]
                if r < b[0]: b[0] = r
                if r > b[1]: b[1] = r
                if c < b[2]: b[2] = c
                if c > b[3]: b[3] = c
    frame = None
    for v, (rmin, rmax, cmin, cmax) in bounds.items():
        if rmax - rmin < 2 or cmax - cmin < 2:
            continue
        ok = True
        for c in range(cmin, cmax + 1):
            if grid[rmin][c] != v or grid[rmax][c] != v:
                ok = False
                break
        if not ok:
            continue
        for r in range(rmin, rmax + 1):
            if grid[r][cmin] != v or grid[r][cmax] != v:
                ok = False
                break
        if ok:
            frame = (v, rmin, rmax, cmin, cmax)
            break
    _, r1, r2, c1, c2 = frame
    interior = [row[c1+1:c2] for row in grid[r1+1:r2]]
    h = len(interior)
    w = len(interior[0]) if h else 0
    res = [[3] * (w + 2) for _ in range(h + 2)]
    for i in range(h):
        for j in range(w):
            res[i+1][j+1] = interior[i][j]
    return res