def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    anchors = {}
    for r in range(h):
        cols = [c for c, v in enumerate(grid[r]) if v == 4]
        if len(cols) >= 2:
            c1, c2 = cols[0], cols[1]
            anchors.setdefault((c1, c2), []).append(r)
    bg = max({v:0 for row in grid for v in row}, key=lambda x: sum(row.count(x) for row in grid))
    sc = max({v:0 for row in grid for v in row if v != bg}, key=lambda x: sum(row.count(x) for row in grid))
    for (c1, c2), rows in anchors.items():
        rows.sort()
        if len(rows) > 2:
            stripe_rows = rows
            ic_map = {}
            r0 = stripe_rows[0]
            vals = []
            for c in range(c1+1, c2):
                v = grid[r0][c]
                if v not in vals:
                    vals.append(v)
            if len(vals) >= 2:
                ic_map[vals[0]] = sc
                ic_map[vals[1]] = bg
            for r in stripe_rows:
                for c in range(c1+1, c2):
                    v = grid[r][c]
                    if v in ic_map:
                        out[r][c] = ic_map[v]
        else:
            if len(rows) == 2:
                stripe_rows = list(range(rows[0]+1, rows[1]))
            else:
                stripe_rows = rows
            ic = [8, 7]
            for r in stripe_rows:
                for c in range(c1+1, c2):
                    out[r][c] = ic[(r + c) % 2]
    return out