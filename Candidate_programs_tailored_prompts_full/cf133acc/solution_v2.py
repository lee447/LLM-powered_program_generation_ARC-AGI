def solve(grid):
    from copy import deepcopy
    g = grid
    n = len(g)
    m = len(g[0])
    bar_rows = []
    for i in range(n):
        s = {g[i][j] for j in range(m) if g[i][j] != 0}
        if len(s) >= 2:
            bar_rows.append(i)
    bar_rows.sort()
    candidates = []
    for c in range(m):
        if all(g[r][c] == 0 for r in bar_rows) and any(g[r][c] != 0 for r in range(n) if r not in bar_rows):
            candidates.append(c)
    candidates.sort()
    c1, c2 = candidates[0], candidates[1]
    spans = []
    for r in bar_rows:
        if c1 > 0 and g[r][c1-1] != 0:
            cl = g[r][c1-1]
        else:
            cl = g[r][c1+1]
        if c2+1 < m and g[r][c2+1] != 0:
            cr = g[r][c2+1]
        else:
            cr = g[r][c2-1]
        spans.append((r, cl, cr))
    spans.sort()
    out = deepcopy(g)
    # fill anchors in bar rows
    for r, cl, cr in spans:
        out[r][c1] = cl
        out[r][c2] = cr
    # fill above first
    if spans:
        r0, cl0, cr0 = spans[0]
        for r in range(0, r0):
            out[r][c1] = cl0
            out[r][c2] = cr0
    # fill between
    for i in range(len(spans)-1):
        _, _, _ = spans[i]
        r_next, cln, crn = spans[i+1]
        for r in range(spans[i][0]+1, r_next):
            out[r][c1] = cln
            out[r][c2] = crn
    return out