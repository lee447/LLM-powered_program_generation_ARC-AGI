def solve(grid):
    H = len(grid)
    W = len(grid[0])
    stripes = []
    for r in range(H):
        for j in range(W - 2):
            c = grid[r][j]
            if c != 0 and grid[r][j + 1] == 0 and grid[r][j + 2] == c:
                stripes.append((r, c, j + 1))
    out = [row[:] for row in grid]
    for r, c, h in stripes:
        if out[r][h] == 0:
            out[r][h] = c
        for i in range(r):
            if out[i][h] == 0:
                out[i][h] = c
    return out