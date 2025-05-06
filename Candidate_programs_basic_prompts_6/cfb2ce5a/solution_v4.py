def solve(grid):
    h, w = len(grid), len(grid[0])
    r0 = next(r for r in range(h) if any(grid[r][c] != 0 for c in range(w)))
    c0 = next(c for c in range(w) if grid[r0][c] != 0)
    N = 0
    while c0+N < w and grid[r0][c0+N] != 0:
        N += 1
    out = [row[:] for row in grid]
    block = [row[c0:c0+N] for row in grid[r0:r0+N]]
    bcols = sorted({v for row in block for v in row})
    for dr in (0, N):
        for dc in (0, N):
            if dr == 0 and dc == 0: continue
            r1, c1 = r0+dr, c0+dc
            if r1+N > h or c1+N > w: continue
            seeds = [(i, j, grid[i][j]) for i in range(r1, r1+N) for j in range(c1, c1+N) if grid[i][j] != 0]
            if not seeds: continue
            mp = {}
            for si, sj, sc in seeds:
                bi = si - r1
                bj = sj - c1
                bv = block[bi][bj]
                if bv not in mp:
                    mp[bv] = sc
            if len(mp) < len(bcols):
                other = [sc for (_, _, sc) in seeds if sc not in mp.values()]
                for bv in bcols:
                    if bv not in mp:
                        mp[bv] = other[0]
            for i in range(N):
                for j in range(N):
                    rr, cc = r1+i, c1+j
                    if out[rr][cc] == 0:
                        out[rr][cc] = mp[block[i][j]]
    return out