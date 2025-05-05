def solve(grid):
    h = len(grid)
    w = len(grid[0])
    res = [row[:] for row in grid]
    anchors = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 4]
    by_row = {}
    for r, c in anchors:
        by_row.setdefault(r, []).append(c)
    for r, cols in by_row.items():
        cols.sort()
        n = len(cols)
        for i in range(n // 2):
            c1 = cols[i]
            c2 = cols[-i - 1]
            for c in range(c1 + 1, c2):
                res[r][c] = 8 if (c == c1 + 1 or c == c2 - 1) else 7
    by_col = {}
    for r, c in anchors:
        by_col.setdefault(c, []).append(r)
    for c, rows in by_col.items():
        rows.sort()
        n = len(rows)
        for i in range(n // 2):
            r1 = rows[i]
            r2 = rows[-i - 1]
            for r in range(r1 + 1, r2):
                res[r][c] = 8 if (r == r1 + 1 or r == r2 - 1) else 7
    return res