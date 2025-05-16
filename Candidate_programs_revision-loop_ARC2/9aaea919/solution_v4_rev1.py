def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    seen = [[False] * w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if not seen[i][j] and grid[i][j] != bg:
                col = grid[i][j]
                pts = [(i, j)]
                seen[i][j] = True
                for y, x in pts:
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < h and 0 <= nx < w and not seen[ny][nx] and grid[ny][nx] == col:
                            seen[ny][nx] = True
                            pts.append((ny, nx))
                y0 = min(y for y, x in pts)
                x0 = min(x for y, x in pts)
                offsets = [(y - y0, x - x0) for y, x in pts]
                clusters.append((y0, x0, col, offsets))
    ys = sorted({y0 for y0, x0, c, off in clusters})
    xs = sorted({x0 for y0, x0, c, off in clusters})
    new = [[bg] * w for _ in range(h)]
    for y0, x0, col, offsets in clusters:
        r = ys.index(y0)
        c = xs.index(x0)
        ny = xs[c]
        nx = ys[r]
        for dy, dx in offsets:
            new[ny + dy][nx + dx] = col
    return new