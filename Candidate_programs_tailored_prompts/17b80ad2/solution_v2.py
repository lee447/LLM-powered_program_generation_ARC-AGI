def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    out = [row[:] for row in grid]
    col_anchors = {}
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v:
                col_anchors.setdefault(j, []).append((i, v))
    for col, lst in col_anchors.items():
        lst.sort(key=lambda x: x[0])
        seq = []
        for _, v in lst:
            if not seq or seq[-1] != v:
                seq.append(v)
        breaks = [max(i for i, v in lst if v == c) for c in seq]
        start = 0
        for c, br in zip(seq, breaks):
            for i in range(start, br + 1):
                out[i][col] = c
            start = br + 1
    return out