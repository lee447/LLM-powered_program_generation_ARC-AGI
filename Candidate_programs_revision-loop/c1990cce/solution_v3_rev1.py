def solve(grid):
    w = len(grid[0])
    c0 = grid[0].index(2)
    L = min(c0, w - 1 - c0)
    N = 2 * L + 1
    out = [[0] * w for _ in range(N)]
    for k in range(L + 1):
        out[k][c0 - k] = 2
        out[k][c0 + k] = 2
    for r in range(L, N):
        d = r - L
        for x in range(-L, L + 1):
            if (d - x) % 4 == 0:
                c = c0 + x
                if 0 <= c < w and out[r][c] == 0:
                    out[r][c] = 1
    return out