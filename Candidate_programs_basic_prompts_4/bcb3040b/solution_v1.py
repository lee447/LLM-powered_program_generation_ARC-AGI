def solve(grid):
    h = len(grid)
    w = len(grid[0])
    pts = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 2:
                pts.append((i, j))
    (r1, c1), (r2, c2) = pts
    dr = 0
    if r2 > r1: dr = 1
    elif r2 < r1: dr = -1
    dc = 0
    if c2 > c1: dc = 1
    elif c2 < c1: dc = -1
    out = [row[:] for row in grid]
    r, c = r1, c1
    while True:
        out[r][c] = 3 if grid[r][c] == 1 else 2
        if r == r2 and c == c2:
            break
        r += dr
        c += dc
    return out