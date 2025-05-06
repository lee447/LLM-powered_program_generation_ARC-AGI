def solve(grid):
    R, C = len(grid), len(grid[0])
    pts = [(r, c) for r in range(R) for c in range(C) if grid[r][c] != 0]
    if not pts:
        return [[0]*C for _ in range(R)]
    ic = grid[pts[0][0]][pts[0][1]]
    r0 = min(r for r,_ in pts)
    r1 = max(r for r,_ in pts)
    c0 = min(c for _,c in pts)
    c1 = max(c for _,c in pts)
    H = r1 - r0 + 1
    W = c1 - c0 + 1
    step = H + W
    primary, secondary = 6, ic
    out = [[0]*C for _ in range(R)]
    for bi in range(0, R, step):
        for bj in range(0, C, step):
            m = bi // step
            n = bj // step
            if (m + n) % 2 == 0:
                for i in range(H):
                    for j in range(W):
                        r, c = bi + i, bj + j
                        if 0 <= r < R and 0 <= c < C:
                            out[r][c] = primary
            else:
                for i in range(W):
                    for j in range(H):
                        r, c = bi + i + H - W + 1, bj + j + W - H + 1
                        if 0 <= r < R and 0 <= c < C:
                            out[r][c] = secondary
    return out