def solve(grid):
    N = len(grid)
    M = (N + 1) // 2
    center = N // 2
    out = [[0] * M for _ in range(M)]
    for i in range(N):
        v1 = grid[i][i]
        if v1:
            if i < center:
                out[0][i] = v1
            elif i == center:
                out[center][center] = v1
            else:
                out[M - 1][i - center] = v1
        v2 = grid[i][N - 1 - i]
        if v2:
            if i < center:
                out[i][M - 1] = v2
            elif i > center:
                out[i - center][0] = v2
    return out