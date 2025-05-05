def solve(grid):
    h, w = len(grid), len(grid[0])
    centers = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 5]
    (r1, c1), (r2, c2) = centers
    up = (r1, c1) if r1 < r2 else (r2, c2)
    down = (r2, c2) if r1 < r2 else (r1, c1)
    left = (r1, c1) if c1 < c2 else (r2, c2)
    right = (r2, c2) if c1 < c2 else (r1, c1)
    r_start = up[0] + 2
    r_end = down[0] - 2
    c_start = left[1]
    c_end = right[1] - 2
    out = [row[:] for row in grid]
    for i in range(r_start, r_end + 1):
        for j in range(c_start, c_end + 1):
            if out[i][j] == 0:
                out[i][j] = 4
    return out