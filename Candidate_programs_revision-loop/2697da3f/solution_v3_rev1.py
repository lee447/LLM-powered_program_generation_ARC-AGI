def solve(grid):
    r0 = len(grid)
    c0 = len(grid[0])
    r1 = 0
    c1 = 0
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v != 0:
                if i < r0: r0 = i
                if i > r1: r1 = i
                if j < c0: c0 = j
                if j > c1: c1 = j
    h = r1 - r0 + 1
    w = c1 - c0 + 1
    D = h if h > w else w
    O = 3 * D if D % 2 else 3 * D - 1
    rp = [0, D, O - D]
    cp = [0, D, O - D]
    out = [[0] * O for _ in range(O)]
    for i in range(h):
        for j in range(w):
            v = grid[r0 + i][c0 + j]
            if v != 0:
                out[rp[1] + i][cp[0] + j] = v
                out[rp[0] + j][cp[1] + i] = v
                out[rp[1] + (h - 1 - i)][cp[2] + (w - 1 - j)] = v
                out[rp[2] + (w - 1 - j)][cp[1] + (h - 1 - i)] = v
    return out