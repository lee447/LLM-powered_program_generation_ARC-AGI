def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    pts = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 1]
    if len(pts) < 2:
        return grid
    pts.sort()
    dr = pts[1][0] - pts[0][0]
    dc = pts[1][1] - pts[0][1]
    new_grid = [row[:] for row in grid]
    r, c = pts[-1]
    while True:
        r += dr
        c += dc
        if not (0 <= r < rows and 0 <= c < cols):
            break
        new_grid[r][c] = 2
    return new_grid