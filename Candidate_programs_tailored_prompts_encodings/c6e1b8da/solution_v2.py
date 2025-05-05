def solve(grid):
    H, W = len(grid), len(grid[0])
    regions = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v != 0:
                if v not in regions:
                    regions[v] = [r, r, c, c]
                else:
                    regions[v][0] = min(regions[v][0], r)
                    regions[v][1] = max(regions[v][1], r)
                    regions[v][2] = min(regions[v][2], c)
                    regions[v][3] = max(regions[v][3], c)
    center_row = H // 2
    for r in range(1, H - 1):
        if all(grid[r][c] == 0 for c in range(W)) and any(grid[r-1][c] != 0 for c in range(W)) and any(grid[r+1][c] != 0 for c in range(W)):
            center_row = r
            break
    center_col = W // 2
    for c in range(1, W - 1):
        if all(grid[r][c] == 0 for r in range(H)) and any(grid[r][c-1] != 0 for r in range(H)) and any(grid[r][c+1] != 0 for r in range(H)):
            center_col = c
            break
    quad_of = {}
    for v, (r0, r1, c0, c1) in regions.items():
        cr = (r0 + r1) / 2
        cc = (c0 + c1) / 2
        vert = 0 if cr < center_row else 2
        hori = 0 if cc < center_col else 1
        quad_of[v] = vert + hori
    order = [0,1,3,2]
    dest = {}
    for v, q in quad_of.items():
        idx = order.index(q)
        new_q = order[(idx+1) % 4]
        dest[v] = new_q
    out = [[0]*W for _ in range(H)]
    for v, (r0, r1, c0, c1) in regions.items():
        h = r1 - r0 + 1
        w = c1 - c0 + 1
        q = dest[v]
        if q in (0,1):
            nr1 = center_row - 1
            nr0 = nr1 - h + 1
        else:
            nr0 = center_row + 1
            nr1 = nr0 + h - 1
        if q in (0,2):
            nc1 = center_col - 1
            nc0 = nc1 - w + 1
        else:
            nc0 = center_col + 1
            nc1 = nc0 + w - 1
        for dr in range(h):
            for dc in range(w):
                out[nr0+dr][nc0+dc] = v
    return out