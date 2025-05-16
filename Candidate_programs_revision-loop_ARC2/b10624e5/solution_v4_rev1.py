def solve(grid):
    h = len(grid)
    w = len(grid[0])
    bg = grid[0][0]
    axis_col = None
    for c in range(w):
        col = [grid[r][c] for r in range(h)]
        if len(set(col)) == 1 and col[0] != bg:
            axis_col = c
            break
    out = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            if c == axis_col: continue
            v = grid[r][c]
            if v != bg:
                mc = 2 * axis_col - c
                if 0 <= mc < w:
                    out[r][mc] = v
    return out