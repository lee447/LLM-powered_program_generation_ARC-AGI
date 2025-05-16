def solve(grid):
    h = len(grid)
    w = len(grid[0])
    counts = {}
    for r in grid:
        for v in r:
            counts[v] = counts.get(v, 0) + 1
    bg = max(counts, key=lambda x: counts[x])
    t = None
    for v in counts:
        if v != bg:
            if t is None or counts[v] < counts[t]:
                t = v
    row_counts = [row.count(t) for row in grid]
    H = max(range(h), key=lambda r: row_counts[r])
    runs = []
    inrun = False
    for c in range(w):
        if grid[H][c] == t:
            if not inrun:
                s = c
                inrun = True
        else:
            if inrun:
                runs.append((s, c - 1))
                inrun = False
    if inrun:
        runs.append((s, w - 1))
    main = max(runs, key=lambda x: x[1] - x[0] + 1)
    S, E = main
    neigh = [r for r in runs if r[0] > E]
    if neigh:
        S2, E2 = min(neigh, key=lambda x: x[0])
    else:
        S2, E2 = None, None
    stripe_cols = []
    for c in range(w):
        cnt = 0
        for r in range(h):
            if r != H and grid[r][c] == t:
                cnt += 1
                if cnt >= 2:
                    stripe_cols.append(c)
                    break
    out = [[bg] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if r == H:
                if grid[r][c] == t or (S <= c <= E) or (S2 is not None and E < c < S2):
                    out[r][c] = t
            else:
                if grid[r][c] == t and c in stripe_cols:
                    out[r][c] = t
    return out