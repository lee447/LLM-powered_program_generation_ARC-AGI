def solve(grid):
    h, w = len(grid), len(grid[0])
    # find bounding box of color 6
    minr, minc, maxr, maxc = h, w, -1, -1
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 6:
                if r < minr: minr = r
                if r > maxr: maxr = r
                if c < minc: minc = c
                if c > maxc: maxc = c
    res = [row[:] for row in grid]
    for r in range(minr, maxr+1):
        for c in range(minc, maxc+1):
            if grid[r][c] == 6:
                # left‐diagonal neighbor
                rr = r+1 if r+1 < h else r
                cc = c-1 if c-1 >= 0 else c
                left = grid[rr][cc]
                # right neighbor (skip block values)
                rc = c+1
                while rc < w and grid[r][rc] == 6:
                    rc += 1
                right = grid[r][rc] if rc < w else grid[r][c]
                # choose
                if (c-minc) < (maxc-c):
                    res[r][c] = left
                else:
                    res[r][c] = right
    return res