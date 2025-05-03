def solve(grid):
    R = len(grid)
    C = len(grid[0])
    H = 2 * R
    W = 2 * C
    out = [[0] * W for _ in range(H)]
    for i in range(H):
        ii = i if i < R else H - 1 - i
        i0 = R - 1 - ii
        for j in range(W):
            jj = j if j < C else W - 1 - j
            j0 = C - 1 - jj
            out[i][j] = grid[i0][j0]
    return out