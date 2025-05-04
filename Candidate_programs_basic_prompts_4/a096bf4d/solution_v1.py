def solve(grid):
    h, w = len(grid), len(grid[0])
    sep_rows = [i for i in range(h) if all(c == 0 for c in grid[i])]
    sep_cols = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    th = sep_rows[1] - sep_rows[0] - 1
    tw = sep_cols[1] - sep_cols[0] - 1
    # reference tile origin
    r0 = sep_rows[0] + 1
    c0 = sep_cols[0] + 1
    # compute background from full reference tile
    cnt = {}
    for i in range(th):
        for j in range(tw):
            v = grid[r0 + i][c0 + j]
            if v != 0:
                cnt[v] = cnt.get(v, 0) + 1
    bg = max(cnt, key=lambda x: cnt[x])
    # central 2x2
    cr = th // 2 - 1
    cc = tw // 2 - 1
    cent = []
    for dr in (0, 1):
        for dc in (0, 1):
            cent.append((dr, dc, grid[r0 + cr + dr][c0 + cc + dc]))
    # find odd one != bg with count==1
    freq = {}
    for _, _, v in cent:
        if v != bg:
            freq[v] = freq.get(v, 0) + 1
    pos = None
    val = None
    for dr, dc, v in cent:
        if v != bg and freq[v] == 1:
            pos = (dr, dc)
            val = v
            break
    if pos is None:
        return grid
    dr, dc = pos
    # propagate
    for bi in range(len(sep_rows) - 1):
        for bj in range(len(sep_cols) - 1):
            r = sep_rows[bi] + 1 + cr + dr
            c = sep_cols[bj] + 1 + cc + dc
            grid[r][c] = val
    return grid