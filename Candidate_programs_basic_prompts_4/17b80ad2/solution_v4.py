def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    out = [[0]*w for _ in range(h)]
    for j in range(w):
        nz = [(i, grid[i][j]) for i in range(h) if grid[i][j] != 0]
        if not nz:
            continue
        nz.sort()
        for k, (i, c) in enumerate(nz):
            start = 0 if k == 0 else nz[k-1][0] + 1
            for r in range(start, i+1):
                out[r][j] = c
    return out