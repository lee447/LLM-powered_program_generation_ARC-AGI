from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    samples = [(r, c) for r in range(h) for c in range(w) if grid[r][c] != 0]
    # detect sample region (two rows of small shapes)
    rows = {}
    for r, c in samples:
        if grid[r][c] != 0:
            rows.setdefault(r, []).append(c)
    sr = sorted(r for r, cols in rows.items() if len(cols) >= 2)
    if len(sr) >= 2:
        r1, r2 = sr[0], sr[1]
        sc1 = sorted(rows[r1])
        sc2 = sorted(rows[r2])
        tl = grid[r1][sc1[0]]
        tr = grid[r1][sc1[1]]
        bl = grid[r2][sc2[0]]
        br = grid[r2][sc2[1]]
    else:
        tl = tr = bl = br = None
    # find frame
    non0 = [(r, c) for r in range(h) for c in range(w) if grid[r][c] != 0]
    best = None
    for r, c in non0:
        col = grid[r][c]
        # try square
        for L in range(1, max(h, w)):
            if r+L < h and c+L < w:
                ok = True
                for x in range(L+1):
                    if grid[r][c+x] != col or grid[r+L][c+x] != col or grid[r+x][c] != col or grid[r+x][c+L] != col:
                        ok = False
                        break
                if ok:
                    best = (r, c, L+1, col)
    if not best:
        return grid
    r0, c0, sz, frm = best
    sub = [row[c0:c0+sz] for row in grid[r0:r0+sz]]
    # remap interior
    vals = sorted({sub[i][j] for i in range(sz) for j in range(sz) if sub[i][j] != frm})
    mp = {}
    if len(vals) == 2:
        mp[vals[0]] = bl
        mp[vals[1]] = tl
    elif len(vals) == 3:
        mp[vals[0]] = bl
        mp[vals[1]] = br
        mp[vals[2]] = tl
    elif len(vals) == 4:
        mp[vals[0]] = bl
        mp[vals[1]] = br
        mp[vals[2]] = tr
        mp[vals[3]] = tl
    else:
        for i, v in enumerate(vals):
            mp[v] = i+1
    out = []
    for i in range(sz):
        row = []
        for j in range(sz):
            v = sub[i][j]
            if v == frm:
                row.append(v)
            elif v in mp and mp[v] is not None:
                row.append(mp[v])
            else:
                row.append(v)
        out.append(row)
    return out