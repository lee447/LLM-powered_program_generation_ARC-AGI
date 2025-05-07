def solve(grid):
    h = len(grid)
    w = len(grid[0])
    pts = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 2:
                pts.append((i, j))
    (r1, c1), (r2, c2) = pts
    dr = (r2 - r1) // abs(r2 - r1) if r2 != r1 else 0
    dc = (c2 - c1) // abs(c2 - c1) if c2 != c1 else 0
    steps = max(abs(r2 - r1), abs(c2 - c1))
    out = [row[:] for row in grid]
    for k in range(steps + 1):
        r = r1 + dr * k
        c = c1 + dc * k
        if grid[r][c] == 1:
            out[r][c] = 3
        else:
            out[r][c] = 2
    return out