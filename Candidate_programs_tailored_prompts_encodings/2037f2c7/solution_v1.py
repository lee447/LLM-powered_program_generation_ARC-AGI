def solve(grid):
    n, m = len(grid), len(grid[0])
    vals = {}
    for i in range(n):
        for j in range(m):
            v = grid[i][j]
            if v != 0:
                vals.setdefault(v, set()).add((i,j))
    # find stripe color: non-zero with smallest unique col span but large row span
    best = None
    for v, cells in vals.items():
        cols = {j for _,j in cells}
        rows = {i for i,_ in cells}
        if len(cols) <= 2 and len(rows) > 1:
            score = (len(rows), -len(cols))
            if best is None or score > best[0]:
                best = (score, v, cols, rows)
    if not best:
        return [[ ]]
    _, stripe_color, stripe_cols, stripe_rows = best
    sc = sorted(stripe_cols)
    # pick leftmost stripe group
    groups = []
    temp = [sc[0]]
    for x in sc[1:]:
        if x == temp[-1] + 1:
            temp.append(x)
        else:
            groups.append(temp)
            temp = [x]
    groups.append(temp)
    stripe_cols = groups[0]
    # stripe rows
    srows = sorted(i for i,j in vals[stripe_color] if j in stripe_cols)
    r0, r1 = srows[0], srows[-1]
    top = r0 - 1
    bot = r1 + 1
    mids = [r0] if len(stripe_cols) == 1 else [r0, r1]
    rows = [top] + mids + [bot]
    # determine cluster bounds from stripe row r0
    row0 = r0
    nz = [j for j in range(m) if grid[row0][j] != 0]
    c0, c1 = min(nz), max(nz)
    h = len(rows)
    w = c1 - c0 + 1
    out = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if i in (0, h-1) or j in (0, w-1):
                out[i][j] = 8
    return out