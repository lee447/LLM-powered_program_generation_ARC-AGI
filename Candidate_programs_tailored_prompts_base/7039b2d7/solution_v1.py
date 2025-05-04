def solve(grid):
    from collections import Counter
    h, w = len(grid), len(grid[0])
    flat = [c for row in grid for c in row]
    bg = Counter(flat).most_common(1)[0][0]
    rows = [i for i in range(h) if len(set(grid[i])) == 1]
    cols = [j for j in range(w) if len({grid[i][j] for i in range(h)}) == 1]
    stripe_color = None
    for i in rows:
        c = grid[i][0]
        if c != bg:
            stripe_color = c
            break
    if stripe_color is None:
        for j in cols:
            c = grid[0][j]
            if c != bg:
                stripe_color = c
                break
    if stripe_color is None:
        stripe_color = bg
    stripe_rows = [i for i in rows if grid[i][0] == stripe_color]
    stripe_cols = [j for j in cols if grid[0][j] == stripe_color]
    stripe_rows.sort()
    stripe_cols.sort()
    if len(stripe_rows) < 2 or len(stripe_cols) < 2:
        return []
    r0, r1 = stripe_rows[0], stripe_rows[1]
    c0, c1 = stripe_cols[0], stripe_cols[1]
    hcell = r1 - r0 - 1
    wcell = c1 - c0 - 1
    if stripe_color != bg:
        fill = bg
    else:
        fill = None
        for i in range(h):
            for j in range(w):
                v = grid[i][j]
                if v != bg:
                    fill = v
                    break
            if fill is not None:
                break
        if fill is None:
            fill = bg
    return [[fill for _ in range(wcell)] for _ in range(hcell)]