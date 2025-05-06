def solve(grid):
    H = len(grid)
    W = len(grid[0])
    stripe_color = None
    for i in range(H):
        v = grid[i][0]
        if all(grid[i][j] == v for j in range(W)):
            stripe_color = v
            break
    row_stripes = [i for i in range(1, H-1) if all(grid[i][j] == stripe_color for j in range(W))]
    col_stripes = [j for j in range(1, W-1) if all(grid[i][j] == stripe_color for i in range(H))]
    R = len(row_stripes) + 1
    C = len(col_stripes) + 1
    rs = set(row_stripes)
    cs = set(col_stripes)
    bg = None
    for i in range(H):
        if i in rs: continue
        for j in range(W):
            if j in cs: continue
            bg = grid[i][j]
            break
        if bg is not None:
            break
    return [[bg]*C for _ in range(R)]