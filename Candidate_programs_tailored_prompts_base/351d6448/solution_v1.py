def solve(grid):
    rows = [i for i, row in enumerate(grid) if any(cell not in (0,5) for cell in row)]
    ncols = len(grid[0])
    segs = []
    for i in rows:
        row = grid[i]
        cols = [j for j, v in enumerate(row) if v not in (0,5)]
        start, end = min(cols), max(cols)
        segs.append((start, end, [row[j] for j in range(start, end+1)]))
    starts = [s for s, e, p in segs]
    ends = [e for s, e, p in segs]
    patterns = [p for s, e, p in segs]
    if len(set(patterns[0])) > 1:
        d = starts[1] - starts[0] if len(starts) > 1 else 0
        nxt_start = starts[-1] + d
        pat = patterns[0]
    else:
        lengths = [e - s + 1 for s, e, p in segs]
        dlen = lengths[1] - lengths[0] if len(lengths) > 1 else 0
        nxt_start = starts[-1]
        pat = [patterns[0][0]] * (lengths[-1] + dlen)
    out = [[0]*ncols for _ in range(3)]
    for i, v in enumerate(pat):
        c = nxt_start + i
        if 0 <= c < ncols:
            out[1][c] = v
    return out