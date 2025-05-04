def solve(grid):
    H = len(grid)
    W = len(grid[0])
    mapping = {0:8,6:7,7:6,8:0}
    out = [row[:] for row in grid]
    rows = []
    for r in range(H):
        if grid[r].count(4) == 2:
            cs = [c for c,v in enumerate(grid[r]) if v == 4]
            c1, c2 = cs
            cnt1 = sum(1 for rr in range(H) if grid[rr][c1] == 4)
            cnt2 = sum(1 for rr in range(H) if grid[rr][c2] == 4)
            if not (cnt1 == 2 and cnt2 == 2):
                rows.append((r, min(c1, c2), max(c1, c2)))
    cols = []
    for c in range(W):
        rs = [r for r in range(H) if grid[r][c] == 4]
        if len(rs) == 2:
            r1, r2 = rs
            cols.append((c, min(r1, r2), max(r1, r2)))
    for r, c1, c2 in rows:
        for c in range(c1+1, c2):
            out[r][c] = mapping.get(out[r][c], out[r][c])
    for c, r1, r2 in cols:
        for r in range(r1+1, r2):
            out[r][c] = mapping.get(out[r][c], out[r][c])
    return out