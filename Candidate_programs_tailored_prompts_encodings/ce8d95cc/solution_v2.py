def solve(grid):
    h, w = len(grid), len(grid[0])
    col_counts = [sum(1 for i in range(h) if grid[i][j] != 0) for j in range(w)]
    row_counts = [sum(1 for j in range(w) if grid[i][j] != 0) for i in range(h)]
    stripes = [j for j, c in enumerate(col_counts) if c == h]
    blocks = [i for i, c in enumerate(row_counts) if c == w]
    stripe_colors = {}
    for j in stripes:
        for i in range(h):
            if grid[i][j] != 0:
                stripe_colors[j] = grid[i][j]
                break
    block_colors = {}
    sset = set(stripes)
    for i in blocks:
        for j in range(w):
            if j not in sset and grid[i][j] != 0:
                block_colors[i] = grid[i][j]
                break
    comp_cols = []
    prev = -1
    for j in sorted(stripes):
        if j - prev > 1:
            comp_cols.append(('bg', None))
        comp_cols.append(('stripe', j))
        prev = j
    if prev < w - 1:
        comp_cols.append(('bg', None))
    comp_rows = []
    prev = -1
    for i in sorted(blocks):
        if i - prev > 1:
            comp_rows.append(('bg', None))
        comp_rows.append(('block', i))
        prev = i
    if prev < h - 1:
        comp_rows.append(('bg', None))
    out = []
    for rtype, ri in comp_rows:
        row = []
        for ctype, cj in comp_cols:
            if ctype == 'stripe':
                row.append(stripe_colors[cj])
            elif rtype == 'block':
                row.append(block_colors[ri])
            else:
                row.append(0)
        out.append(row)
    return out