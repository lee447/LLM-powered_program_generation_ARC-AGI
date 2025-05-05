def solve(grid):
    h, w = len(grid), len(grid[0])
    motif_rows = sorted(r for r in range(h) if any(0 < grid[r][c] != 5 for c in range(w)))
    motifs = []
    for r in motif_rows:
        cols = [c for c in range(w) if grid[r][c] != 0 and grid[r][c] != 5]
        motifs.append((cols, [grid[r][c] for c in cols]))
    is_translation = any(len(set(colors)) > 1 for _, colors in motifs)
    if is_translation:
        starts = [cols[0] for cols, _ in motifs]
        d = starts[1] - starts[0]
        new_start = starts[-1] + d
        base_cols, base_colors = motifs[0]
        deltas = [c - base_cols[0] for c in base_cols]
        new_row = [0]*w
        for delta, val in zip(deltas, base_colors):
            new_row[new_start + delta] = val
    else:
        lengths = [len(cols) for cols, _ in motifs]
        d = lengths[1] - lengths[0]
        new_len = lengths[-1] + d
        start = motifs[0][0][0]
        val = motifs[0][1][0]
        new_row = [val if start <= c < start + new_len else 0 for c in range(w)]
    empty = [0]*w
    return [empty, new_row, empty]