def solve(grid):
    h, w = len(grid), len(grid[0])
    stripes = []
    for r in range(h):
        c = 0
        while c < w:
            if grid[r][c] == 4:
                start = c
                while c < w and grid[r][c] == 4:
                    c += 1
                length = c - start
                if length >= 3:
                    stripes.append((r, start, c - 1))
            else:
                c += 1
    stripes.sort()
    r0, c0, c1 = stripes[0]
    c_mid = (c0 + c1) // 2
    # find first row below stripe with non-zero under stripe center
    r = r0 + 1
    while r < h and all(grid[r][x] == 0 for x in range(c0, c1 + 1)):
        r += 1
    if r == h:
        return []
    # determine horizontal extents from that row
    row0 = r
    cmin, cmax = w, -1
    for x in range(w):
        if grid[row0][x] != 0:
            cmin = min(cmin, x)
            cmax = max(cmax, x)
    # collect contiguous rows
    rows = []
    while r < h:
        if any(grid[r][x] != 0 for x in range(cmin, cmax + 1)):
            rows.append(r)
            r += 1
        else:
            break
    if not rows:
        return []
    rmin, rmax = rows[0], rows[-1]
    H = rmax - rmin + 1
    W = cmax - cmin + 1
    out = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if i in (0, H - 1) or j in (0, W - 1):
                out[i][j] = 8
    return out