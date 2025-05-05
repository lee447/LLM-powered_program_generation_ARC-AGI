def solve(grid):
    H = len(grid)
    W = len(grid[0])
    background = 0
    stripe_cols = []
    for j in range(W):
        counts = {}
        for i in range(H):
            v = grid[i][j]
            counts[v] = counts.get(v, 0) + 1
        mc = max(counts.items(), key=lambda x: x[1])[0]
        if mc != background:
            stripe_cols.append(j)
    rep_rows = [0]
    seen = set()
    # background row color
    for j in range(W):
        if j not in stripe_cols:
            seen.add(grid[0][j])
            break
    for i in range(1, H):
        vs = None
        ok = True
        for j in range(W):
            if j in stripe_cols: continue
            if vs is None:
                vs = grid[i][j]
            elif grid[i][j] != vs:
                ok = False
                break
        if ok and vs not in seen:
            rep_rows.append(i)
            seen.add(vs)
    desc_rows = []
    if len(rep_rows) >= 2:
        desc_rows.append(('band', rep_rows[0]))
        desc_rows.append(('band', rep_rows[1]))
        for r in rep_rows[2:]:
            desc_rows.append(('spacer', None))
            desc_rows.append(('band', r))
        desc_rows.append(('spacer', None))
    else:
        for r in rep_rows:
            desc_rows.append(('band', r))
    desc_cols = [('spacer', None)]
    for j in stripe_cols:
        desc_cols.append(('stripe', j))
        desc_cols.append(('spacer', None))
    # bandColors and stripeColors
    band_colors = {}
    for kind, r in desc_rows:
        if kind == 'band':
            for j in range(W):
                if j not in stripe_cols:
                    band_colors[r] = grid[r][j]
                    break
    stripe_colors = {}
    ref = rep_rows[0]
    for j in stripe_cols:
        stripe_colors[j] = grid[ref][j]
    bgc = band_colors[rep_rows[0]]
    R = len(desc_rows)
    C = len(desc_cols)
    out = [[0]*C for _ in range(R)]
    for i in range(R):
        rk, rv = desc_rows[i]
        for j in range(C):
            ck, cv = desc_cols[j]
            if rk == 'band' and ck == 'stripe':
                out[i][j] = grid[rv][cv]
            elif rk == 'band' and ck == 'spacer':
                out[i][j] = band_colors[rv]
            elif rk == 'spacer' and ck == 'stripe':
                out[i][j] = stripe_colors[cv]
            else:
                out[i][j] = bgc
    return out