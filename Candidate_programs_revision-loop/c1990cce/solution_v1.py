def solve(grid):
    w = len(grid[0])
    row = grid[0]
    c0 = row.index(2)
    L = min(c0, w - 1 - c0)
    N = 2 * L + 1
    out = [[0] * w for _ in range(N)]
    # draw red arms
    for k in range(L + 1):
        out[k][c0 - k] = 2
        out[k][c0 + k] = 2
    # draw blue arms
    for k in range(1, L + 1):
        r = L + k
        out[r][c0 - k] = 1
        out[r][c0 + k] = 1
    return out