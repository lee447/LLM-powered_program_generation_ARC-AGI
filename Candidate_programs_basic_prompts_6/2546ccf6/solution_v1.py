def solve(grid):
    H = len(grid)
    W = len(grid[0])
    g = [row[:] for row in grid]
    vseps = sorted(c for c in range(W) if len({g[r][c] for r in range(H)}) == 1 and g[0][c] != 0)
    hseps = sorted(r for r in range(H) if len({g[r][c] for c in range(W)}) == 1 and g[r][0] != 0)
    col_ranges = []
    prev = -1
    for c in vseps:
        if prev + 1 <= c - 1:
            col_ranges.append((prev + 1, c - 1))
        prev = c
    if prev + 1 <= W - 1:
        col_ranges.append((prev + 1, W - 1))
    row_ranges = []
    prev = -1
    for r in hseps:
        if prev + 1 <= r - 1:
            row_ranges.append((prev + 1, r - 1))
        prev = r
    if prev + 1 <= H - 1:
        row_ranges.append((prev + 1, H - 1))
    for r0, r1 in row_ranges:
        if len(col_ranges) < 2: break
        c0, c1 = col_ranges[0]
        c2, c3 = col_ranges[1]
        p0 = [(r, c) for r in range(r0, r1+1) for c in range(c0, c1+1) if g[r][c] != 0 and g[r][c] == g[r0][c0] or (g[r][c] != 0 and g[r][c] not in (0, g[r0][c0]) and ((r,c) in [(rr,cc) for rr in range(r0,r1+1) for cc in range(c0,c1+1)]))]
        p0 = [(r, c) for r, c in p0 if g[r][c] != (g[r0][c0] if g[r0][c0] != 0 else None)]
        p0 = [(r, c) for r, c in p0 if g[r][c] != 0 and g[r][c] != (g[r][c0] if (g[r][c0] != 0) else None)]
        p0 = [(r, c) for r, c in p0 if g[r][c] != 0]
        p0 = [(r, c) for r, c in p0 if c0 <= c <= c1]
        p1 = [(r, c) for r in range(r0, r1+1) for c in range(c2, c3+1) if g[r][c] != 0]
        if not p0 and not p1:
            continue
        if p0:
            sc = g[p0[0][0]][p0[0][1]]
        else:
            sc = g[p1[0][0]][p1[0][1]]
        if p0 and not p1:
            for r in range(r0, r1+1):
                for c in range(c2, c3+1):
                    if g[r][c] == sc:
                        g[r][c] = 0
            for r, c in p0:
                cnew = c2 + (c1 - c)
                g[r][cnew] = sc
        elif p1 and not p0:
            for r in range(r0, r1+1):
                for c in range(c0, c1+1):
                    if g[r][c] == sc:
                        g[r][c] = 0
            for r, c in p1:
                cnew = c0 + (c3 - c)
                g[r][cnew] = sc
    return g