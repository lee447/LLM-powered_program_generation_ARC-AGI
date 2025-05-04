def solve(grid):
    H, W = len(grid), len(grid[0])
    out = [[0]*W for _ in range(H)]
    t = 1
    r0, c0 = t, t
    w = 0
    while c0+w < W and grid[r0][c0+w] != 0:
        w += 1
    h = 0
    while r0+h < H and grid[r0+h][c0] != 0:
        h += 1
    for i in range(h):
        for j in range(w):
            out[r0+i][c0+j] = grid[r0+i][c0+j]
    br0, bc0 = r0, c0+w
    seeds = []
    for i in range(h):
        for j in range(w):
            v = grid[br0+i][bc0+j]
            if v != 0 and v not in seeds:
                seeds.append(v)
    def pick(i,j):
        a = seeds[0]
        b = seeds[1] if len(seeds)>1 else a
        return a if ((i+j)&1)==0 else b
    for i in range(h):
        for j in range(w):
            out[br0+i][bc0+j] = pick(i,j)
    lower = []
    for i in range(r0+h, H-t):
        for j in range(c0, W-t):
            v = grid[i][j]
            if v != 0:
                lower.append(v)
    lower.sort()
    idx = 0
    for i in range(r0+h, H-t):
        for j in range(c0, c0+w):
            if idx < len(lower):
                out[i][j] = lower[idx]
                idx += 1
    for i in range(H):
        for j in range(W):
            if out[i][j] == 0:
                out[i][j] = 0
    return out