def solve(grid):
    R = len(grid)
    C = len(grid[0])
    stripe_cols = {j for j in range(C) if grid[R-1][j] != 0}
    out = [[0]*C for _ in range(R)]
    for j in stripe_cols:
        anchors = [(i, grid[i][j]) for i in range(R) if grid[i][j] != 0]
        anchors.sort()
        prev = 0
        for i, v in anchors:
            for k in range(prev, i+1):
                out[k][j] = v
            prev = i+1
    for i in range(R):
        for j in range(C):
            if j not in stripe_cols and grid[i][j] != 0:
                out[i][j] = grid[i][j]
    return out