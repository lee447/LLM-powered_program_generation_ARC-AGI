def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    comps = {}
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v != bg:
                if v not in comps: comps[v] = [j, j]
                comps[v][0] = min(comps[v][0], j)
                comps[v][1] = max(comps[v][1], j)
    items = sorted([(comps[c][1] - comps[c][0] + 1, c) for c in comps])
    widths = [iw for iw, _ in items]
    colors = [ic for _, ic in items]
    diffs = [widths[0]] + [widths[i] - widths[i-1] for i in range(1, len(widths))]
    rows = len(widths) * 2
    cols = widths[-1]
    out = [[0]*cols for _ in range(rows)]
    for r in range(rows):
        b = r * len(widths) // rows
        for i in range(len(diffs)):
            for c in range(sum(diffs[:i]), sum(diffs[:i+1])):
                if c < cols:
                    out[r][c] = colors[i]
    return out