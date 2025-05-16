def solve(grid):
    h, w = len(grid), len(grid[0])
    freq = {}
    for r in grid:
        for v in r:
            freq[v] = freq.get(v, 0) + 1
    bg = max(freq, key=freq.get)
    rows = [i for i in range(h) if any(grid[i][j] != bg for j in range(w))]
    if not rows:
        return grid
    rows.sort()
    groups = []
    cur = [rows[0]]
    for r in rows[1:]:
        if r == cur[-1] + 1:
            cur.append(r)
        else:
            groups.append(cur)
            cur = [r]
    groups.append(cur)
    best = None
    best_sum = -1
    for g in groups:
        if len(g) >= 2:
            s = sum(sum(1 for j in range(w) if grid[r][j] != bg) for r in g)
            if s > best_sum:
                best_sum = s
                best = g
    if best is None:
        return grid
    idx = groups.index(best)
    if idx == 0:
        return grid
    src = best
    dest = groups[idx - 1]
    mid_src = src[len(src) // 2]
    mid_dest = dest[len(dest) // 2]
    out = [row[:] for row in grid]
    for j in range(w):
        if grid[mid_src][j] != bg:
            out[mid_dest][j] = grid[mid_src][j]
    return out