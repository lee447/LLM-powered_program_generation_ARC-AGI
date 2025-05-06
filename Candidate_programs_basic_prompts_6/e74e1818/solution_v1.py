def solve(grid):
    h = len(grid)
    if h == 0: return []
    w = len(grid[0])
    res = [[0]*w for _ in range(h)]
    rows_by_color = {}
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v:
                rows_by_color.setdefault(v, set()).add(i)
    for c, rows in rows_by_color.items():
        rows = sorted(rows)
        m = len(rows)
        for idx, src in enumerate(rows):
            dst = rows[m-1-idx]
            for j in range(w):
                if grid[src][j] == c:
                    res[dst][j] = c
    return res