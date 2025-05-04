def solve(grid):
    row = grid[0]
    N = len(row)
    k = row.index(2)
    out = [[0]*N for _ in range(N)]
    for r in range(N):
        if r <= k:
            c1 = k - r
            c2 = k + r
            out[r][c1] = 2
            out[r][c2] = 2
    for t in range((N - 3) // 2 + 1):
        r0 = 3 + 2*t
        c0 = k - 1 - 2*t
        if 0 <= c0 < N:
            r, c = r0, c0
            while r < N and c < N:
                if out[r][c] == 0:
                    out[r][c] = 1
                r += 1; c += 1
    return out