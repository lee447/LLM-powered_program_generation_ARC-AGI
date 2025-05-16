def solve(grid):
    h, w = len(grid), len(grid[0])
    H = W = 20
    hh, ww = h // 2, w // 2
    out = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            a = (i + (j // w) * hh) % h
            b = (j + (i // h) * ww) % w
            out[i][j] = grid[a][b]
    return out