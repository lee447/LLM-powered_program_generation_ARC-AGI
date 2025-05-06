def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import defaultdict, deque
    cells = defaultdict(list)
    order = []
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v:
                if v not in cells:
                    order.append(v)
                cells[v].append((r, c))
    mids = []
    for v in order:
        pts = cells[v]
        minr = min(r for r, c in pts)
        maxr = max(r for r, c in pts)
        minc = min(c for r, c in pts)
        maxc = max(c for r, c in pts)
        mids.append((minr, minc, maxr, maxc, v))
    first = mids[0]
    side = {}
    if first[0] == 0:
        side[first[4]] = 'R'
        side[mids[1][4]] = 'L'
    else:
        side[first[4]] = 'L'
        side[mids[1][4]] = 'R'
    res = [[0]*w for _ in range(h)]
    for minr, minc, maxr, maxc, v in mids:
        pts = cells[v]
        drs = [r-minr for r, c in pts]
        dcs = [c-minc for r, c in pts]
        if side[v] == 'L':
            offc = 0 - minc
        else:
            offc = (w-1 - maxc)
        if minr == 0:
            offr = h//2 - minr
        else:
            offr = 0 - minr
        for (r, c), dr, dc in zip(pts, drs, dcs):
            nr = r + offr
            nc = c + offc
            res[nr][nc] = v
    return res