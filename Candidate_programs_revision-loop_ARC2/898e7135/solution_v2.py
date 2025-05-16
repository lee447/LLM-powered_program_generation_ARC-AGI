def solve(grid):
    h = len(grid)
    w = len(grid[0])
    cnt = {}
    for r in grid:
        for c in r:
            cnt[c] = cnt.get(c, 0) + 1
    # ignore background 0
    nonzero = [c for c in cnt if c != 0]
    # pick noise as the color with smallest non-zero count
    noise = min(nonzero, key=lambda c: cnt[c])
    # gather clusters of other colors
    clusters = []
    for c in sorted(nonzero):
        if c == noise:
            continue
        pts = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == c]
        if not pts:
            continue
        rs = [p[0] for p in pts]
        cs_ = [p[1] for p in pts]
        r0, r1 = min(rs), max(rs)
        c0, c1 = min(cs_), max(cs_)
        shape = [[c for _ in range(c0, c1+1)] for __ in range(r0, r1+1)]
        clusters.append((r0 + c0, c, shape))
    # sort by bounding-box top-left sum
    clusters.sort(key=lambda x: x[0])
    shapes = [s for _, _, s in clusters]
    cols = [c for _, c, _ in clusters]
    # background color = most frequent nonzero
    bg = max(nonzero, key=lambda c: cnt[c])
    # prepare quadrant tiling
    b = 2
    n = len(shapes)
    # get dims
    hs = [len(s) for s in shapes]
    ws = [len(s[0]) for s in shapes]
    # quadrant order: TL, TR, BR, BL
    # compute max widths/heights
    wL = max(ws[0] if n>0 else 0, ws[3] if n>3 else 0)
    wR = max(ws[1] if n>1 else 0, ws[2] if n>2 else 0)
    hT = max(hs[0] if n>0 else 0, hs[1] if n>1 else 0)
    hB = max(hs[2] if n>2 else 0, hs[3] if n>3 else 0)
    interior = max(wL + wR, hT + hB)
    H = interior + 2*b
    W = interior + 2*b
    out = [[bg]*W for _ in range(H)]
    # placement offsets
    pos = []
    if n>0:
        pos.append((b, b))
    if n>1:
        pos.append((b, b + interior - ws[1]))
    if n>2:
        pos.append((b + interior - hs[2], b + interior - ws[2]))
    if n>3:
        pos.append((b + interior - hs[3], b))
    for i, shape in enumerate(shapes[:4]):
        r0, c0 = pos[i]
        for di in range(len(shape)):
            for dj in range(len(shape[0])):
                out[r0+di][c0+dj] = shape[di][dj]
    return out