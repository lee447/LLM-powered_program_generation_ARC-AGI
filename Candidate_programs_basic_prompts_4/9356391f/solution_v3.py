def solve(grid):
    h, w = len(grid), len(grid[0])
    first_row = grid[0]
    k = max(i for i, v in enumerate(first_row) if v != 0)
    cr = cc = None
    bg = grid[1][0]
    for i in range(2, h):
        for j in range(w):
            if grid[i][j] != 0 and grid[i][j] != bg:
                cr, cc = i, j
                break
        if cr is not None:
            break
    out = [row[:] for row in grid]
    for dy in range(-k, k+1):
        for dx in range(-k, k+1):
            m = max(abs(dy), abs(dx))
            if m <= k:
                r, c = cr + dy, cc + dx
                if 0 <= r < h and 0 <= c < w:
                    out[r][c] = first_row[m]
    return out