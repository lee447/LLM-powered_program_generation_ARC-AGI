def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    ones = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 1]
    ones.sort(key=lambda x: (x[0], x[1]))
    (r0, c0), (r1, c1) = ones[0], ones[1]
    dr, dc = r1 - r0, c1 - c0
    r_last, c_last = ones[-1]
    new_grid = [row[:] for row in grid]
    r_new, c_new = r_last + dr, c_last + dc
    while 0 <= r_new < h and 0 <= c_new < w:
        new_grid[r_new][c_new] = 2
        r_new += dr
        c_new += dc
    return new_grid