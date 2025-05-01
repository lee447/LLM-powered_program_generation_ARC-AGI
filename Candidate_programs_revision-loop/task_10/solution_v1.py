def solve(grid):
    h, w = len(grid), len(grid[0])
    rmin = h; rmax = -1; cmin = w; cmax = -1
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 0:
                if r < rmin: rmin = r
                if r > rmax: rmax = r
                if c < cmin: cmin = c
                if c > cmax: cmax = c
    res = [[0]*w for _ in range(h)]
    pattern = [0, -1, 0, 1]
    for i, r in enumerate(range(rmin, rmax+1)):
        shift = pattern[i % 4]
        for c in range(cmin, cmax+1):
            v = grid[r][c]
            if v != 0:
                res[r][c + shift] = v
    return res