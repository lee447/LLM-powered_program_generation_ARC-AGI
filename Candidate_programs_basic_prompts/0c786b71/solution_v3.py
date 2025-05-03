def solve(grid):
    R = len(grid)
    C = len(grid[0])
    A = [[grid[R-1-i][C-1-j] for j in range(C)] for i in range(R)]
    H = 2 * R
    W = 2 * C
    out = [[0] * W for _ in range(H)]
    for i in range(H):
        mi = i if i < R else H - 1 - i
        for j in range(W):
            mj = j if j < C else W - 1 - j
            out[i][j] = A[mi][mj]
    return out