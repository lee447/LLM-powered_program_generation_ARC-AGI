def solve(grid):
    H, W = len(grid), len(grid[0])
    minr, maxr, minc, maxc = H, -1, W, -1
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0:
                minr = min(minr, i)
                maxr = max(maxr, i)
                minc = min(minc, j)
                maxc = max(maxc, j)
    h_in, w_in = maxr - minr + 1, maxc - minc + 1
    c_in = grid[minr][minc]
    c_out = 3 if c_in == 6 else 6
    P = h_in + w_in
    out = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            di = (i - minr) % P
            dj = (j - minc) % P
            if di < h_in and dj < w_in:
                out[i][j] = c_in
            elif di >= h_in and dj >= w_in:
                out[i][j] = c_out
    return out