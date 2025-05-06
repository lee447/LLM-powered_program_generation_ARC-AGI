def solve(grid):
    from math import isqrt
    n, m = len(grid), len(grid[0])
    cnt = {}
    for r in grid:
        for v in r:
            cnt[v] = cnt.get(v, 0) + 1
    d = None
    B = None
    for v, c in cnt.items():
        s = isqrt(c)
        if s * s == c and n % s == 0 and m % s == 0:
            # check bounding box size s*s
            rows = [i for i in range(n) for j in range(m) if grid[i][j] == v]
            if not rows: continue
            cols = [j for i in range(n) for j in range(m) if grid[i][j] == v]
            r0, r1 = min(rows), max(rows)
            c0_, c1 = min(cols), max(cols)
            if (r1 - r0 + 1) == s and (c1 - c0_ + 1) == s:
                d, B = v, s
                R0, C0 = r0, c0_
                break
    if d is None:
        return grid
    rows_blk = n // B
    cols_blk = m // B
    i0, j0 = R0 // B, C0 // B
    j1 = cols_blk - 1 - j0
    new = [row[:] for row in grid]
    for dr in range(B):
        for dc in range(B):
            new[R0+dr][C0+dc] = grid[i0*B+dr][j1*B + (B-1-dc)]
    return new