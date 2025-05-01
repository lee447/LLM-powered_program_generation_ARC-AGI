def solve(grid):
    h, w = len(grid), len(grid[0])
    pts = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] != 0]
    rs = [r for r, c, v in pts]
    cs = [c for r, c, v in pts]
    rmin, rmax, cmin, cmax = min(rs), max(rs), min(cs), max(cs)
    cr = (rmin + rmax) / 2
    cc = (cmin + cmax) / 2
    s2 = 2 ** 0.5
    out = [[0] * w for _ in range(h)]
    for r, c, v in pts:
        dr = r - cr
        dc = c - cc
        nr = cr + (dr - dc) / s2
        nc = cc + (dr + dc) / s2
        rr = int(round(nr))
        cc2 = int(round(nc))
        if 0 <= rr < h and 0 <= cc2 < w:
            out[rr][cc2] = v
    return out