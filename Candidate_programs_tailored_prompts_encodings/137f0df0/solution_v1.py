def solve(grid):
    H = len(grid)
    W = len(grid[0])
    # find cluster size
    cluster_h = cluster_w = None
    for r in range(H - 1):
        for c in range(W - 1):
            if grid[r][c] == 5:
                # measure width
                cw = 1
                while c + cw < W and grid[r][c + cw] == 5:
                    cw += 1
                # measure height
                ch = 1
                while r + ch < H and grid[r + ch][c] == 5:
                    ch += 1
                if cw > 1 and ch > 1:
                    cluster_h, cluster_w = ch, cw
                    break
        if cluster_h is not None:
            break
    # find top-lefts of clusters
    tops = []
    for r in range(H - cluster_h + 1):
        for c in range(W - cluster_w + 1):
            ok = True
            for dr in range(cluster_h):
                for dc in range(cluster_w):
                    if grid[r+dr][c+dc] != 5:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                continue
            if (r > 0 and grid[r-1][c] == 5) or (c > 0 and grid[r][c-1] == 5):
                continue
            tops.append((r, c))
    # row bands and col bands
    rs = sorted({r for r, _ in tops})
    cs = sorted({c for _, c in tops})
    # covered rows and cols
    covered_r = set()
    for r in rs:
        for dr in range(cluster_h):
            covered_r.add(r+dr)
    covered_c = set()
    for c in cs:
        for dc in range(cluster_w):
            covered_c.add(c+dc)
    # blank segments for rows
    row_segs = []
    r = 0
    while r < H:
        if r not in covered_r:
            s = r
            while r+1 < H and (r+1) not in covered_r:
                r += 1
            row_segs.append((s, r))
        r += 1
    # blank segments for cols
    col_segs = []
    c = 0
    while c < W:
        if c not in covered_c:
            s = c
            while c+1 < W and (c+1) not in covered_c:
                c += 1
            col_segs.append((s, c))
        c += 1
    # stripe and border segments
    stripe_rows = []
    border_rows = []
    for s, e in row_segs:
        if s > 0 and e < H-1:
            stripe_rows.extend(range(s, e+1))
        else:
            border_rows.extend(range(s, e+1))
    stripe_cols = []
    border_cols = []
    for s, e in col_segs:
        if s > 0 and e < W-1:
            stripe_cols.extend(range(s, e+1))
        else:
            border_cols.extend(range(s, e+1))
    # copy grid
    out = [row[:] for row in grid]
    # draw red stripes
    for r in stripe_rows:
        for c in range(W):
            if out[r][c] == 0:
                out[r][c] = 2
    for c in stripe_cols:
        for r in range(H):
            if out[r][c] == 0:
                out[r][c] = 2
    # draw blue at intersections with border segments
    for r in stripe_rows:
        for c in border_cols:
            if out[r][c] == 2:
                out[r][c] = 1
    for c in stripe_cols:
        for r in border_rows:
            if out[r][c] == 2:
                out[r][c] = 1
    return out