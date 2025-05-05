def solve(grid):
    h = len(grid)
    w = len(grid[0])
    centers = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 3:
                if 0 < r < h-1 and 0 < c < w-1:
                    if grid[r-1][c] == 3 and grid[r+1][c] == 3 and grid[r][c-1] == 3 and grid[r][c+1] == 3:
                        centers.append((r, c))
    res = [row[:] for row in grid]
    for i in range(len(centers)):
        r1, c1 = centers[i]
        for j in range(i+1, len(centers)):
            r2, c2 = centers[j]
            dr = r2 - r1
            dc = c2 - c1
            if abs(dr) == abs(dc) and dr != 0:
                step_r = (dr > 0) - (dr < 0)
                step_c = (dc > 0) - (dc < 0)
                r, c = r1 + step_r, c1 + step_c
                while (r, c) != (r2, c2):
                    if res[r][c] == 0:
                        res[r][c] = 2
                    r += step_r
                    c += step_c
    return res