def solve(grid):
    H, W = len(grid), len(grid[0])
    nz = [(r, c) for r in range(H) for c in range(W) if grid[r][c] != 0]
    nz.sort()
    r0, c0 = nz[0]
    # find block size by scanning right and down
    w = 0
    while c0 + w < W and grid[r0][c0 + w] != 0:
        w += 1
    h = 0
    while r0 + h < H and grid[r0 + h][c0] != 0:
        h += 1
    N = min(w, h)
    # extract block pattern and its two colors
    block = [row[c0:c0+N] for row in grid[r0:r0+N]]
    colors = sorted({v for row in block for v in row})
    a, b = colors
    # helper to pick first two nonzero in region
    def pick2(rs, re, cs, ce):
        s = []
        for i in range(rs, re):
            for j in range(cs, ce):
                v = grid[i][j]
                if v != 0 and v not in s:
                    s.append(v)
                    if len(s) == 2:
                        return s
        return s
    # TR seeds: rows r0..r0+N, cols > c0+N-1
    tr = pick2(r0, r0+N, c0+N, W)
    bl = pick2(r0+N, H, c0, c0+N)
    # BR cluster seeds coords
    br_pts = [(i - (r0+N), j - (c0+N), grid[i][j])
              for i in range(r0+N, H) for j in range(c0+N, W)
              if grid[i][j] != 0]
    if br_pts:
        drs = [d for d, _, _ in [(d,c,v) for d,c,v in br_pts]]
        dcs = [c for _, c, _ in [(d,c,v) for d,c,v in br_pts]]
        tile_h = max(drs) - min(drs) + 1
        tile_w = max(dcs) - min(dcs) + 1
    else:
        tile_h = tile_w = 1
    out = [[0]*W for _ in range(H)]
    # copy border zeros and TL block
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 0:
                continue
    for i in range(N):
        for j in range(N):
            out[r0+i][c0+j] = grid[r0+i][c0+j]
    # map block colors to tr
    if len(tr) < 2: tr = (tr + tr)[:2]
    for i in range(N):
        for j in range(N):
            v = block[i][j]
            m = tr[0] if v == a else tr[1]
            out[r0+i][c0+N+j] = m
    # map block colors to bl
    if len(bl) < 2: bl = (bl + bl)[:2]
    for i in range(N):
        for j in range(N):
            v = block[i][j]
            m = bl[0] if v == a else bl[1]
            out[r0+N+i][c0+j] = m
    # stamp br cluster
    for dr, dc, v in br_pts:
        for ti in range(N // tile_h + 1):
            for tj in range(N // tile_w + 1):
                i = r0+N + dr + ti*tile_h
                j = c0+N + dc + tj*tile_w
                if r0+N <= i < r0+N+N and c0+N <= j < c0+N+N:
                    out[i][j] = v
    return out