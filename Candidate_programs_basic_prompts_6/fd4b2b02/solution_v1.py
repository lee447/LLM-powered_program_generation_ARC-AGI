def solve(grid):
    H, W = len(grid), len(grid[0])
    pts = [(i,j) for i in range(H) for j in range(W) if grid[i][j] != 0]
    C = grid[pts[0][0]][pts[0][1]]
    r0, c0 = min(i for i,_ in pts), min(j for _,j in pts)
    r1, c1 = max(i for i,_ in pts), max(j for _,j in pts)
    h, w = r1 - r0 + 1, c1 - c0 + 1
    S0 = [[1]*w for _ in range(h)]
    S90 = list(zip(*S0[::-1]))
    C2 = 3 if C == 6 else 6
    stride = h + w
    ti = -(-r0 // stride)
    tj = -(-c0 // stride)
    by = r0 - ti*stride
    bx = c0 - tj*stride
    out = [[0]*W for _ in range(H)]
    for i in range(ti+4):
        for j in range(tj+4):
            orien = (i+j) % 2 == 0
            shape = S0 if orien else S90
            ch = C if orien else C2
            sh, sw = len(shape), len(shape[0])
            ys, xs = i*stride + by, j*stride + bx
            for di in range(sh):
                for dj in range(sw):
                    y, x = ys+di, xs+dj
                    if 0 <= y < H and 0 <= x < W and shape[di][dj]:
                        out[y][x] = ch
    return out