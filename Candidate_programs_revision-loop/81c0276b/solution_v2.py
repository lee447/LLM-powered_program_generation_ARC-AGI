def solve(grid):
    # find separator rows and cols
    rows, cols = len(grid), len(grid[0])
    sep_rows = {r for r in range(rows) if len(set(grid[r]))==1 and grid[r][0]!=0}
    sep_cols = {c for c in range(cols) if len({grid[r][c] for r in range(rows)})==1 and grid[0][c]!=0}
    # find block row spans
    brs = []
    r = 0
    while r < rows:
        if r in sep_rows:
            r += 1
            continue
        start = r
        while r<rows and r not in sep_rows:
            r+=1
        brs.append((start, r))
    # find block col spans
    bcs = []
    c = 0
    while c < cols:
        if c in sep_cols:
            c += 1
            continue
        start = c
        while c<cols and c not in sep_cols:
            c+=1
        bcs.append((start, c))
    # build blockMatrix of shapes
    block = []
    for rs, re in brs:
        rowv = []
        for cs, ce in bcs:
            val = 0
            # scan for 2x2 subblock non-separator & non-zero
            for i in (rs, rs+1):
                for j in (cs, cs+1):
                    if grid[i][j]!=0 and grid[i][j] not in sep_cols and grid[i][j] not in sep_rows:
                        val = grid[i][j]
            rowv.append(val)
        block.append(rowv)
    # count shape colors
    cnt = {}
    for row in block:
        for v in row:
            if v!=0:
                cnt[v] = cnt.get(v,0)+1
    # sort colors by freq asc, value desc
    cols_sorted = sorted(cnt.items(), key=lambda x:(x[1],-x[0]))
    colors = [c for c,_ in cols_sorted]
    h = len(colors)
    w = len(bcs)
    out = [[0]*w for _ in range(h)]
    for r in range(h):
        fill = colors[r]
        end = w if r==h-1 else r+1
        for c in range(end):
            out[r][c] = fill
    return out