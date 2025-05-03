def solve(grid):
    m = len(grid)
    n = len(grid[0]) if m else 0
    ones = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                ones.append((i, j))
    if len(ones) < 2:
        return grid
    ones.sort()
    dr = ones[1][0] - ones[0][0]
    dc = ones[1][1] - ones[0][1]
    out = [row[:] for row in grid]
    r, c = ones[-1]
    while True:
        r += dr
        c += dc
        if not (0 <= r < m and 0 <= c < n):
            break
        if out[r][c] == 0:
            out[r][c] = 2
    return out