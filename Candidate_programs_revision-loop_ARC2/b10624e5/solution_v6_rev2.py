def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    axis = next(c for c in range(w) if len({grid[r][c] for r in range(h)}) == 1 and grid[0][c] != bg)
    out = [row[:] for row in grid]
    for r in range(h):
        for c in range(axis):
            v = grid[r][c]
            if v != bg:
                mc = 2 * axis - c
                if 0 <= mc < w:
                    out[r][mc] = v
    return out