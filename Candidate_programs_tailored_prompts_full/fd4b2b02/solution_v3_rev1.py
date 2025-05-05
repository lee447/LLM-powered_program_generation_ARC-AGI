def solve(grid):
    R, C = len(grid), len(grid[0])
    r0, r1, c0, c1 = R, -1, C, -1
    for i in range(R):
        for j in range(C):
            if grid[i][j] != 0:
                r0 = min(r0, i); r1 = max(r1, i)
                c0 = min(c0, j); c1 = max(c1, j)
    h, w = r1 - r0 + 1, c1 - c0 + 1
    oc = grid[r0][c0]
    nc = 3 if oc == 6 else 6
    T = h + w
    out = [[0]*C for _ in range(R)]
    for k in range((R + T - 1)//T + 1):
        for m in range((C + T - 1)//T + 1):
            sr = h - 1 + k*T
            sc = h - w + m*T
            for di in range(w):
                for dj in range(h):
                    i, j = sr + di, sc + dj
                    if 0 <= i < R and 0 <= j < C:
                        out[i][j] = nc
            sr2 = h - w + k*T
            sc2 = h - 1 + m*T
            for di in range(h):
                for dj in range(w):
                    i, j = sr2 + di, sc2 + dj
                    if 0 <= i < R and 0 <= j < C:
                        out[i][j] = oc
    return out