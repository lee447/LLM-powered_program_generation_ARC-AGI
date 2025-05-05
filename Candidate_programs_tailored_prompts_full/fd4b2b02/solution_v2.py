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
    h_rot, w_rot = w_in, h_in
    out = [[0]*W for _ in range(H)]
    def fill(r, c, h, w, v):
        for i in range(h):
            for j in range(w):
                out[r+i][c+j] = v
    fill(0, 0, h_rot, w_rot, c_out)
    fill(0, W-w_rot, h_rot, w_rot, c_out)
    fill(H-h_rot, 0, h_rot, w_rot, c_out)
    fill(H-h_rot, W-w_rot, h_rot, w_rot, c_out)
    co = (W - w_in)//2
    ro = (H - h_in)//2
    fill(0, co, h_in, w_in, c_in)
    fill(H-h_in, co, h_in, w_in, c_in)
    fill(ro, 0, h_in, w_in, c_in)
    fill(ro, W-w_in, h_in, w_in, c_in)
    return out