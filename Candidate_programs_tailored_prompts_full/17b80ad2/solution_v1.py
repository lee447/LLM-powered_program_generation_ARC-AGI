def solve(grid):
    import bisect
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    last = h - 1
    for c in range(w):
        if grid[last][c] != 0:
            rows = [r for r in range(h) if grid[r][c] != 0]
            for r in range(h):
                if grid[r][c] == 0:
                    i = bisect.bisect_left(rows, r)
                    if i < len(rows):
                        out[r][c] = grid[rows[i]][c]
                    else:
                        out[r][c] = grid[rows[-1]][c]
    return out