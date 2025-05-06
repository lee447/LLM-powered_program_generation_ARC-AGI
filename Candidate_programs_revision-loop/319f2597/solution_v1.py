def solve(grid):
    r0 = len(grid)
    r1 = -1
    c0 = len(grid[0])
    c1 = -1
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v == 0:
                if i < r0: r0 = i
                if i > r1: r1 = i
                if j < c0: c0 = j
                if j > c1: c1 = j
    preserved = 2
    R, C = len(grid), len(grid[0])
    out = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if r0 <= i <= r1 or c0 <= j <= c1:
                out[i][j] = grid[i][j] if grid[i][j] == preserved else 0
            else:
                out[i][j] = grid[i][j]
    return out