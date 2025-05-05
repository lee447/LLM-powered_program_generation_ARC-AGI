def solve(grid):
    R, C = len(grid), len(grid[0])
    pts = [(r, c) for r in range(R) for c in range(C) if grid[r][c] != 0]
    if not pts:
        return [[0]*C for _ in range(R)]
    cols = {grid[r][c] for r,c in pts}
    c0 = cols.pop()
    c1 = (cols or {3,6}).pop() if cols else (3 if c0==6 else 6)
    min_r = min(r for r,c in pts)
    min_c = min(c for r,c in pts)
    max_r = max(r for r,c in pts)
    max_c = max(c for r,c in pts)
    h = max_r - min_r + 1
    w = max_c - min_c + 1
    S = h + w
    delta = {(r-min_r, c-min_c) for r,c in pts}
    rot = {(c-min_c, h-1-(r-min_r)) for r,c in pts}
    out = [[0]*C for _ in range(R)]
    for r in range(R):
        kr = (r - min_r) // S
        dr = (r - min_r) - kr*S
        for c in range(C):
            kc = (c - min_c) // S
            dc = (c - min_c) - kc*S
            if (kr + kc) % 2 == 0:
                if 0 <= dr < h and 0 <= dc < w and (dr,dc) in delta:
                    out[r][c] = c0
                elif h <= dr < S and w <= dc < S and (dr-h,dc-w) in rot:
                    out[r][c] = c1
    return out