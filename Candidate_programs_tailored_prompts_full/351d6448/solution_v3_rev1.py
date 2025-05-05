def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    segs = []
    for i, row in enumerate(grid):
        if any(cell not in (0,5) for cell in row):
            starts = [j for j,cell in enumerate(row) if cell not in (0,5)]
            if starts:
                start = starts[0]
                vals = []
                j = start
                while j < cols and grid[i][j] not in (0,5):
                    vals.append(grid[i][j])
                    j += 1
                segs.append((i, start, len(vals), vals))
    segs.sort(key=lambda x: x[0])
    starts = [s for _,s,_,_ in segs]
    lengths = [l for _,_,l,_ in segs]
    last_start, last_len, last_vals = starts[-1], lengths[-1], segs[-1][3]
    if len(starts) > 1:
        delta_start = starts[1] - starts[0]
        delta_len = lengths[1] - lengths[0]
    else:
        delta_start = delta_len = 0
    new_start = last_start + delta_start
    new_len = last_len + delta_len
    new_vals = [last_vals[i % len(last_vals)] for i in range(new_len)]
    out = [[0]*cols for _ in range(3)]
    for k, v in enumerate(new_vals):
        idx = new_start + k
        if 0 <= idx < cols:
            out[1][idx] = v
    return out