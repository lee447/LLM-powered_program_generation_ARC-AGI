def solve(grid):
    h, w = len(grid), len(grid[0])
    centers = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 3:
                if 0 < r < h-1 and 0 < c < w-1:
                    if grid[r-1][c] == 3 and grid[r+1][c] == 3 and grid[r][c-1] == 3 and grid[r][c+1] == 3:
                        centers.append((r, c))
    out = [row[:] for row in grid]
    n = len(centers)
    for i in range(n):
        r1, c1 = centers[i]
        for j in range(i+1, n):
            r2, c2 = centers[j]
            dr = r2 - r1
            dc = c2 - c1
            if dr and abs(dr) == abs(dc):
                step_r = 1 if dr > 0 else -1
                step_c = 1 if dc > 0 else -1
                r, c = r1 + step_r, c1 + step_c
                while (r, c) != (r2, c2):
                    if out[r][c] == 0:
                        out[r][c] = 2
                    r += step_r
                    c += step_c
    return out