def solve(grid):
    N = len(grid)
    M = (N + 1) // 2
    cb = N // 2
    cs = M // 2
    out = [[0] * M for _ in range(M)]
    for i in range(N):
        v1 = grid[i][i]
        if v1:
            if i < cb:
                out[0][i] = v1
            elif i == cb:
                out[cs][cs] = v1
            else:
                out[M - 1][i - cb] = v1
        v2 = grid[i][N - 1 - i]
        if v2:
            if i < cb:
                out[i][M - 1] = v2
            elif i > cb:
                out[i - cb][0] = v2
    return out