def solve(grid):
    h = len(grid)
    w = len(grid[0])
    endpoints = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 2]
    if len(endpoints) != 2:
        return grid
    (r1, c1), (r2, c2) = endpoints
    dr = 0 if r1 == r2 else (1 if r2 > r1 else -1)
    dc = 0 if c1 == c2 else (1 if c2 > c1 else -1)
    res = [row[:] for row in grid]
    r, c = r1, c1
    while True:
        orig = grid[r][c]
        if orig != 2:
            res[r][c] = 2 if orig == 0 else 3
        else:
            res[r][c] = 2
        if (r, c) == (r2, c2):
            break
        r += dr
        c += dc
    return res