def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    anchors = []
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 0 and v != 1:
                anchors.append((r, c, v))
    anchors.sort(key=lambda x:(x[0], x[1]))
    vals = [v for _, _, v in anchors]
    modules = []
    for r in range(h-1):
        for c in range(w-1):
            if grid[r][c]==1 and grid[r][c+1]==1 and grid[r+1][c]==1 and grid[r+1][c+1]==1:
                modules.append((r, c))
    modules.sort()
    out = [row[:] for row in grid]
    for (r, c), v in zip(modules, vals):
        out[r][c] = v
        out[r][c+1] = v
        out[r+1][c] = v
        out[r+1][c+1] = v
    return out