def solve(grid):
    rows, cols = len(grid), len(grid[0])
    sep_rows = [r for r in range(rows) if all(grid[r][c] == 4 for c in range(cols))]
    sep_cols = [c for c in range(cols) if all(grid[r][c] == 4 for r in range(rows))]
    h = sep_rows[1] - sep_rows[0] - 1
    w = sep_cols[1] - sep_cols[0] - 1
    r0, c0 = sep_rows[0] + 1, sep_cols[0] + 1
    colors = set()
    for dr in range(h):
        for dc in range(w):
            v = grid[r0 + dr][c0 + dc]
            if v not in (0, 1, 4):
                colors.add(v)
    motif_color = colors.pop() if colors else None
    motif = [(dr, dc) for dr in range(h) for dc in range(w)
             if motif_color is not None and grid[r0 + dr][c0 + dc] == motif_color]
    res = [row[:] for row in grid]
    for i in range(len(sep_rows) - 1):
        for j in range(len(sep_cols) - 1):
            br, bc = sep_rows[i] + 1, sep_cols[j] + 1
            for dr, dc in motif:
                res[br + dr][bc + dc] = motif_color
    return res