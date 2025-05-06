def solve(grid):
    h = len(grid)
    w = len(grid[0])
    res = [row[:] for row in grid]
    last = h - 1
    stripes = [c for c in range(w) if grid[last][c] != 0]
    for c in stripes:
        pts = [(r, grid[r][c]) for r in range(h) if grid[r][c] != 0]
        pts.sort()
        rows = [r for r, v in pts]
        vals = [v for r, v in pts]
        for r in range(h):
            if grid[r][c] == 0:
                if r < rows[0]:
                    res[r][c] = vals[0]
                elif r > rows[-1]:
                    res[r][c] = vals[-1]
                else:
                    for rr, vv in pts:
                        if rr > r:
                            res[r][c] = vv
                            break
    return res