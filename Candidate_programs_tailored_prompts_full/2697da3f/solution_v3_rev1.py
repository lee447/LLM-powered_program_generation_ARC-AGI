def solve(grid):
    R, C = len(grid), len(grid[0])
    pts = [(r, c) for r in range(R) for c in range(C) if grid[r][c] != 0]
    r0 = min(r for r, _ in pts)
    r1 = max(r for r, _ in pts)
    c0 = min(c for _, c in pts)
    c1 = max(c for _, c in pts)
    H, W = r1 - r0 + 1, c1 - c0 + 1
    N = min(H, W)
    S = 0 if H == W else 1
    row_shift = (H - N + 1) // 2 if H > W else 0
    col_shift = (W - N + 1) // 2 if W > H else 0
    motif = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            motif[i][j] = grid[r0 + row_shift + i][c0 + col_shift + j]
    step = N + S
    M = 3 * N + 2 * S
    out = [[0] * M for _ in range(M)]
    for bi in range(3):
        for bj in range(3):
            if (bi == 1) ^ (bj == 1):
                oi, oj = bi * step, bj * step
                for i in range(N):
                    for j in range(N):
                        v = motif[i][j]
                        if v:
                            out[oi + i][oj + j] = v
    return out