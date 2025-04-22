def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    pts = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 1]
    if len(pts) < 2:
        return grid
    pts.sort()
    dr = pts[1][0] - pts[0][0]
    dc = pts[1][1] - pts[0][1]
    res = [row[:] for row in grid]
    r, c = pts[-1][0] + dr, pts[-1][1] + dc
    while 0 <= r < h and 0 <= c < w:
        res[r][c] = 2
        r += dr
        c += dc
    return res