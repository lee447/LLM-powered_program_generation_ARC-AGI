def solve(grid):
    H = len(grid)
    W = len(grid[0]) if H else 0
    block_rows = []
    for r in range(H):
        for v in grid[r]:
            if v != 0 and v != 5:
                block_rows.append(r)
                break
    starts, lengths, segments = [], [], []
    for r in block_rows:
        cols = [c for c in range(W) if grid[r][c] not in (0, 5)]
        if not cols: continue
        starts.append(cols[0])
        lengths.append(len(cols))
        segments.append([grid[r][c] for c in cols])
    if len(starts) > 1:
        dx = starts[1] - starts[0]
        if any(starts[i+1] - starts[i] != dx for i in range(len(starts)-1)):
            dx = 0
    else:
        dx = 0
    if len(lengths) > 1:
        dl = lengths[1] - lengths[0]
        if any(lengths[i+1] - lengths[i] != dl for i in range(len(lengths)-1)):
            dl = 0
    else:
        dl = 0
    next_start = starts[-1] + dx
    next_len = lengths[-1] + dl
    pattern = list(segments[-1])
    if dl > 0:
        pattern += [pattern[-1]] * dl
    out = [[0] * W for _ in range(3)]
    for i, v in enumerate(pattern):
        c = next_start + i
        if 0 <= c < W:
            out[1][c] = v
    return out