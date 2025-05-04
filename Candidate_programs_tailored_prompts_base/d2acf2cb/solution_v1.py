def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    anchors = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 4]
    rows_set = sorted({r for r, _ in anchors})
    cols_set = sorted({c for _, c in anchors})
    out = [list(row) for row in grid]
    if len(rows_set) == 2 and len(cols_set) == 2:
        r0, r1 = rows_set
        c0, c1 = cols_set
        for r in range(r0 + 1, r1):
            if r == r0 + 1:
                vL, vR = 8, 8
            elif r <= r1 - 2:
                vL, vR = 8, 7
            else:
                vL, vR = 7, 8
            out[r][c0] = vL
            out[r][c1] = vR
    else:
        for r in rows_set:
            cs = sorted(c for rr, c in anchors if rr == r)
            if len(cs) != 2:
                continue
            lo, hi = cs
            uniq = {grid[r][c] for c in range(lo + 1, hi) if grid[r][c] != 4}
            if uniq == {0, 6}:
                mp = {0: 8, 6: 7}
            elif uniq == {7, 8}:
                mp = {7: 6, 8: 0}
            else:
                mp = {}
            for c in range(lo + 1, hi):
                v = grid[r][c]
                if v in mp:
                    out[r][c] = mp[v]
    return out