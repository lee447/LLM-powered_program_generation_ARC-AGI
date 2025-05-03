def solve(grid):
    h = len(grid)
    w = len(grid[0])
    B = [row[::-1] for row in grid[::-1]]
    H, W = 2*h, 2*w
    out = [[0]*W for _ in range(H)]
    for r in range(H):
        r0 = r if r < h else H-1-r
        for c in range(W):
            c0 = c if c < w else W-1-c
            out[r][c] = B[r0][c0]
    return out