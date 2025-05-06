def solve(grid):
    H = len(grid)
    W = len(grid[0])
    counts = {}
    for i in range(H):
        for j in range(W):
            v = grid[i][j]
            if v:
                counts[v] = counts.get(v, 0) + 1
    region_vals = sorted(counts, key=lambda x: -counts[x])[:2]
    r0 = H; r1 = -1; c0 = W; c1 = -1
    for i in range(H):
        for j in range(W):
            if grid[i][j] in region_vals:
                if i < r0: r0 = i
                if i > r1: r1 = i
                if j < c0: c0 = j
                if j > c1: c1 = j
    N = r1 - r0 + 1
    region = [grid[r0 + i][c0:c0+N] for i in range(N)]
    mTR = {}
    mBL = {}
    mBR = {}
    for i in range(H):
        for j in range(W):
            v = grid[i][j]
            if v and not (r0 <= i <= r1 and c0 <= j <= c1):
                if r0 <= i <= r1 and c1 < j <= c1 + N:
                    ri = i - r0
                    cj = j - (c1 + 1)
                    oi = ri
                    oj = N - 1 - cj
                    mTR[region[oi][oj]] = v
                if r1 < i <= r1 + N and c0 <= j <= c1:
                    ri = i - (r1 + 1)
                    cj = j - c0
                    oi = N - 1 - ri
                    oj = cj
                    mBL[region[oi][oj]] = v
                if r1 < i <= r1 + N and c1 < j <= c1 + N:
                    ri = i - (r1 + 1)
                    cj = j - (c1 + 1)
                    oi = N - 1 - ri
                    oj = N - 1 - cj
                    mBR[region[oi][oj]] = v
    out = [row[:] for row in grid]
    for i in range(N):
        for j in range(N):
            out[r0 + i][c1 + 1 + j] = mTR[region[i][N-1-j]]
            out[r1 + 1 + i][c0 + j] = mBL[region[N-1-i][j]]
            out[r1 + 1 + i][c1 + 1 + j] = mBR[region[N-1-i][N-1-j]]
    return out