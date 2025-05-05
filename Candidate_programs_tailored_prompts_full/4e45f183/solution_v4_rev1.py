def solve(grid):
    h, w = len(grid), len(grid[0])
    row_seps = [i for i in range(h) if all(v == 0 for v in grid[i])]
    col_seps = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    row_ranges, prev = [], -1
    for r in row_seps:
        if r - prev > 1:
            row_ranges.append(list(range(prev + 1, r)))
        prev = r
    col_ranges, prev = [], -1
    for c in col_seps:
        if c - prev > 1:
            col_ranges.append(list(range(prev + 1, c)))
        prev = c
    R, C = len(row_ranges), len(col_ranges)
    blocks = [[None] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            rows, cols = row_ranges[i], col_ranges[j]
            cnt = {}
            for r in rows:
                for c in cols:
                    v = grid[r][c]
                    if v != 0:
                        cnt[v] = cnt.get(v, 0) + 1
            a, b = list(cnt.items())
            c1, c2 = a[0], b[0]
            if cnt[c1] > cnt[c2]:
                bg, ac = c1, c2
            else:
                bg, ac = c2, c1
            shape = []
            for dr, r in enumerate(rows):
                for dc, c in enumerate(cols):
                    if grid[r][c] == ac:
                        shape.append((dr, dc))
            blocks[i][j] = (bg, ac, shape)
    out = [row[:] for row in grid]
    for i in range(R):
        for j in range(C):
            bg0, ac0, shape0 = blocks[i][(j - 1) % C]
            bg1, ac1 = ac0, bg0
            rows, cols = row_ranges[i], col_ranges[j]
            for r in rows:
                for c in cols:
                    out[r][c] = bg1
            for dr, dc in shape0:
                out[rows[dr]][cols[dc]] = ac1
    return out