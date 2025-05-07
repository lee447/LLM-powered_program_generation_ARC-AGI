def solve(grid):
    R, C = len(grid), len(grid[0])
    pts = [(i, j) for i in range(R) for j in range(C) if grid[i][j] != 0]
    if not pts:
        return [[0]*C for _ in range(R)]
    rows = [i for i,_ in pts]; cols = [j for _,j in pts]
    r0, r1 = min(rows), max(rows)
    c0, c1 = min(cols), max(cols)
    h = r1 - r0 + 1; w = c1 - c0 + 1
    C0 = grid[r0][c0]; D = 9 - C0
    T = h + w
    r_off_v = r0 % T; c_off_v = c0 % T
    r_off_h = (r_off_v - w) % T; c_off_h = (c_off_v + w) % T
    out = [[0]*C for _ in range(R)]
    for i0 in range(r_off_v, R, T):
        for j0 in range(c_off_v, C, T):
            for di in range(h):
                for dj in range(w):
                    i, j = i0+di, j0+dj
                    if 0 <= i < R and 0 <= j < C:
                        out[i][j] = C0
    for i0 in range(r_off_h, R, T):
        for j0 in range(c_off_h, C, T):
            for di in range(w):
                for dj in range(h):
                    i, j = i0+di, j0+dj
                    if 0 <= i < R and 0 <= j < C:
                        out[i][j] = D
    return out