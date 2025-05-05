def solve(grid):
    h = len(grid)
    w = len(grid[0])
    min_r = h; max_r = -1; min_c = w; max_c = -1
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 0:
                if r < min_r: min_r = r
                if r > max_r: max_r = r
                if c < min_c: min_c = c
                if c > max_c: max_c = c
    axis_r2 = min_r + max_r
    axis_c2 = min_c + max_c
    shape_cells = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] != 0]
    is_horiz = True
    for r, c, v in shape_cells:
        r2 = axis_r2 - r
        if not (0 <= r2 < h and grid[r2][c] == v):
            is_horiz = False
            break
    is_vert = True
    for r, c, v in shape_cells:
        c2 = axis_c2 - c
        if not (0 <= c2 < w and grid[r][c2] == v):
            is_vert = False
            break
    axis_row = axis_r2 // 2 if axis_r2 % 2 == 0 else axis_r2 // 2 + 1
    axis_col = axis_c2 // 2 if axis_c2 % 2 == 0 else axis_c2 // 2 + 1
    out = [row[:] for row in grid]
    if is_horiz and all(grid[axis_row][c] == 0 for c in range(w)):
        for c in range(w):
            out[axis_row][c] = 3
    elif is_vert and all(grid[r][axis_col] == 0 for r in range(h)):
        for r in range(h):
            out[r][axis_col] = 3
    return out