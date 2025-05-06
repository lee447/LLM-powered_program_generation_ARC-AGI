def solve(grid):
    h = len(grid)
    w = len(grid[0])
    stripes = {j for j in range(w) if grid[h-1][j] != 0}
    res = [[0]*w for _ in range(h)]
    for j in stripes:
        last = 0
        for i in range(h-1, -1, -1):
            if grid[i][j] != 0:
                last = grid[i][j]
                res[i][j] = grid[i][j]
            else:
                res[i][j] = last
    for i in range(h):
        for j in range(w):
            if j not in stripes:
                res[i][j] = grid[i][j]
    return res