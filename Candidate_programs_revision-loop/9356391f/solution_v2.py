def solve(grid):
    h, w = len(grid), len(grid[0])
    cy = cx = None
    for y in range(2, h):
        for x in range(w):
            if grid[y][x] != 0:
                cy, cx = y, x
                break
        if cy is not None:
            break
    for r in range(w):
        c = grid[0][r]
        for d in range(-r, r + 1):
            y1, x1 = cy - r, cx + d
            y2, x2 = cy + r, cx + d
            y3, x3 = cy + d, cx - r
            y4, x4 = cy + d, cx + r
            if 0 <= y1 < h and 0 <= x1 < w:
                grid[y1][x1] = c
            if 0 <= y2 < h and 0 <= x2 < w:
                grid[y2][x2] = c
            if 0 <= y3 < h and 0 <= x3 < w:
                grid[y3][x3] = c
            if 0 <= y4 < h and 0 <= x4 < w:
                grid[y4][x4] = c
    return grid