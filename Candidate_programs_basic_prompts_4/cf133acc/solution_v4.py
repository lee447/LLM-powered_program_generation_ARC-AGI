def solve(grid):
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    for color in range(1, 10):
        rows = {}
        cols = {}
        for i in range(h):
            for j in range(w):
                if grid[i][j] == color:
                    rows.setdefault(i, []).append(j)
                    cols.setdefault(j, []).append(i)
        for i, js in rows.items():
            a, b = min(js), max(js)
            for j in range(a, b + 1):
                out[i][j] = color
        for j, is_ in cols.items():
            a, b = min(is_), max(is_)
            for i in range(a, b + 1):
                out[i][j] = color
    return out