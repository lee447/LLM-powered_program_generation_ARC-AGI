def solve(grid):
    h = len(grid)
    w = len(grid[0])
    pts = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2]
    (r1, c1), (r2, c2) = pts
    dr = (r2 > r1) - (r2 < r1)
    dc = (c2 > c1) - (c2 < c1)
    out = [row[:] for row in grid]
    r, c = r1, c1
    while True:
        if (r, c) != (r1, c1) and (r, c) != (r2, c2):
            out[r][c] = 3 if grid[r][c] == 1 else 2
        if (r, c) == (r2, c2):
            break
        r += dr
        c += dc
    return out