def solve(grid):
    h, w = len(grid), len(grid[0])
    coords = [(r, c) for r in range(h) for c in range(w) if grid[r][c] != 0]
    if not coords:
        return grid
    values = sorted({grid[r][c] for r, c in coords})
    v = values[0]
    pts = sorted([(r, c) for r, c in coords if grid[r][c] == v])
    if len(pts) < 2:
        return grid
    dr = pts[1][0] - pts[0][0]
    dc = pts[1][1] - pts[0][1]
    r, c = pts[-1]
    new_val = v + 1
    while True:
        r += dr
        c += dc
        if 0 <= r < h and 0 <= c < w:
            grid[r][c] = new_val
        else:
            break
    return grid