def solve(grid):
    d = {}
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v:
                d.setdefault(v, []).append((i, j))
    cluster_val = None
    lines = []
    for v, pts in d.items():
        if len(pts) < 3:
            cluster_val = v
        else:
            lines.append(v)
    lines.sort(key=lambda v: len(d[v]), reverse=True)
    outer, inner = lines[0], lines[1]
    size = len(d[outer])
    out = [[0]*size for _ in range(size)]
    for off, col in enumerate((outer, inner)):
        for x in range(off, size-off):
            out[off][x] = col
            out[size-1-off][x] = col
            out[x][off] = col
            out[x][size-1-off] = col
    off = 2
    for i in range(off, size-off):
        for j in range(off, size-off):
            out[i][j] = cluster_val
    return out