def solve(grid):
    h = len(grid)
    w = len(grid[0])
    res = [row.copy() for row in grid]
    for r in range(h):
        row = grid[r]
        zeros = [c for c,v in enumerate(row) if v==0]
        if not zeros: continue
        positions = [c for c,v in enumerate(row) if v!=0]
        if not positions: continue
        for p in range(1, w+1):
            pat = {}
            ok = True
            for c in positions:
                k = c % p
                v = row[c]
                if k in pat:
                    if pat[k] != v:
                        ok = False
                        break
                else:
                    pat[k] = v
            if ok:
                break
        for c in zeros:
            res[r][c] = pat[c % p]
    return res