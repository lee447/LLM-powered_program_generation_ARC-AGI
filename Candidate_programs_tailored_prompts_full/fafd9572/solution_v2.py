def solve(grid):
    h = len(grid)
    w = len(grid[0])
    modules = []
    cells = set()
    for r in range(h - 1):
        for c in range(w - 1):
            if grid[r][c] == 1 and grid[r+1][c] == 1 and grid[r][c+1] == 1 and grid[r+1][c+1] == 1:
                modules.append((r, c))
                cells |= {(r, c), (r+1, c), (r, c+1), (r+1, c+1)}
    anchors = []
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v not in (0, 1) and (r, c) not in cells:
                anchors.append((r, c, v))
    modules.sort()
    anchors.sort(key=lambda x: (x[0], x[1]))
    vals = [v for _, _, v in anchors]
    out = [row[:] for row in grid]
    for (r, c), v in zip(modules, vals):
        for dr in (0, 1):
            for dc in (0, 1):
                out[r+dr][c+dc] = v
    return out