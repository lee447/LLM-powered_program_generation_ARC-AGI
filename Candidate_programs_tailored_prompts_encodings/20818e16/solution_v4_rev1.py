import bisect
def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    comps = {}
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v != bg:
                if v not in comps:
                    comps[v] = [j, j]
                else:
                    comps[v][0] = min(comps[v][0], j)
                    comps[v][1] = max(comps[v][1], j)
    items = sorted([(comps[c][1] - comps[c][0] + 1, c) for c in comps])
    widths = [iw for iw, _ in items]
    colors = [c for _, c in items]
    diffs = [widths[0]] + [widths[i] - widths[i-1] for i in range(1, len(widths))]
    prefix = []
    s = 0
    for d in diffs:
        s += d
        prefix.append(s)
    n = len(colors)
    rows = n * 2
    cols = prefix[-1]
    out = [[0]*cols for _ in range(rows)]
    for r in range(rows):
        b = r * n // rows
        if b >= n:
            b = n - 1
        for c in range(cols):
            k = bisect.bisect_right(prefix, c)
            if k < n and c < prefix[k]:
                pass
            else:
                k = n - 1
            if k < b:
                k = b
            out[r][c] = colors[k]
    return out