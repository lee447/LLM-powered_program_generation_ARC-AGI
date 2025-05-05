def solve(grid):
    g = [row[:] for row in grid]
    zeros = [i for i, row in enumerate(g) if all(v == 0 for v in row)]
    bands = []
    for i in range(len(zeros) - 1):
        s = zeros[i] + 1
        e = zeros[i + 1] - 1
        if s <= e:
            bands.append((s, e))
    n = len(bands)
    if n == 2:
        h_b = v_b = 2
    elif n >= 3:
        h_b = n - 1
        v_b = n
    else:
        h_b = v_b = -1
    for idx, (sr, er) in enumerate(bands, start=1):
        row = g[sr]
        col0 = next(c for c, v in enumerate(row) if v != 0)
        color = g[sr][col0]
        cr = sr + 2
        cc = col0 + 2
        if idx == h_b:
            for c in range(col0 + 1, col0 + 4):
                g[cr][c] = color
        if idx == v_b:
            for r in range(sr + 1, sr + 4):
                g[r][cc] = color
    return g