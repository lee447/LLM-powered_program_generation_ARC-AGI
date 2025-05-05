def solve(grid):
    H = len(grid)
    W = len(grid[0])
    # find background color as most frequent
    freq = {}
    for r in grid:
        for v in r:
            freq[v] = freq.get(v, 0) + 1
    bg_color = max(freq, key=lambda k: freq[k])
    # find stripe columns
    stripe_cols = []
    for c in range(W):
        non_bg = 0
        for r in range(H):
            if grid[r][c] != bg_color:
                non_bg += 1
        if non_bg > H // 2:
            stripe_cols.append(c)
    stripe_cols.sort()
    # find band rows
    non_stripe = [c for c in range(W) if c not in stripe_cols]
    seen = set()
    band_rows = []
    band_colors = []
    for r in range(H):
        if non_stripe:
            v0 = grid[r][non_stripe[0]]
            ok = True
            for c in non_stripe:
                if grid[r][c] != v0:
                    ok = False
                    break
            if not ok:
                continue
            if v0 not in seen:
                seen.add(v0)
                band_rows.append(r)
                band_colors.append(v0)
    m = len(band_rows)
    # find stripe colors for spacer
    stripe_colors = []
    br_set = set(band_rows)
    for c in stripe_cols:
        v = bg_color
        for r in range(H):
            if r not in br_set:
                v = grid[r][c]
                break
        stripe_colors.append(v)
    # compute spans for columns
    spans = []
    prev = -1
    for c in stripe_cols:
        spans.append((prev + 1, c - 1))
        prev = c
    spans.append((stripe_cols[-1] + 1, W - 1))
    # compute stripe positions and output width
    stripe_pos = []
    col_idx = 0
    for i in range(len(stripe_cols)):
        a, b = spans[i]
        if b >= a:
            col_idx += 1
        stripe_pos.append(col_idx)
        col_idx += 1
    a, b = spans[-1]
    if b >= a:
        col_idx += 1
    cols_out = col_idx
    # build row sequence
    seq = []
    if m >= 1:
        seq.append(("band", 0))
    if m >= 2:
        seq.append(("band", 1))
    for i in range(2, m):
        seq.append(("spacer", None))
        seq.append(("band", i))
    # after last band, spacer if any band beyond second
    if m >= 2:
        seq.append(("spacer", None))
    # build output
    out = []
    for typ, idx in seq:
        row = [band_colors[0]] * cols_out
        if typ == "band":
            r0 = band_rows[idx]
            for j, pc in enumerate(stripe_pos):
                row[pc] = grid[r0][stripe_cols[j]]
        else:  # spacer
            for j, pc in enumerate(stripe_pos):
                row[pc] = stripe_colors[j]
        out.append(row)
    return out