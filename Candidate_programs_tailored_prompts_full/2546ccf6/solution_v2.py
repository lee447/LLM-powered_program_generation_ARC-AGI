def solve(grid):
    h, w = len(grid), len(grid[0])
    stripe_rows = []
    stripe_cols = []
    for i in range(h):
        s = set(grid[i])
        if len(s) == 1 and grid[i][0] != 0:
            stripe_rows.append(i)
    for j in range(w):
        s = {grid[i][j] for i in range(h)}
        if len(s) == 1 and next(iter(s)) != 0:
            stripe_cols.append(j)
    stripe_rows.sort()
    stripe_cols.sort()
    r0, r1, r2 = stripe_rows[0], stripe_rows[1], stripe_rows[2]
    c0, c1, c2 = stripe_cols[0], stripe_cols[1], stripe_cols[2]
    br = [(r0 + 1, r1), (r1 + 1, r2)]
    bc = [(c0 + 1, c1), (c1 + 1, c2)]
    shapes = {}
    for i in (0, 1):
        for j in (0, 1):
            rs, re = br[i]
            cs, ce = bc[j]
            shape = []
            for r in range(rs, re):
                for c in range(cs, ce):
                    v = grid[r][c]
                    if v != 0:
                        shape.append((r - rs, c - cs, v))
            shapes[(i, j)] = shape
    out = [row[:] for row in grid]
    for j in (0, 1):
        s0 = shapes[(0, j)]
        s1 = shapes[(1, j)]
        for i in (0, 1):
            rs, re = br[i]
            cs, ce = bc[j]
            for r in range(rs, re):
                for c in range(cs, ce):
                    out[r][c] = 0
        for dr, dc, v in s1:
            out[br[0][0] + dr][bc[j][0] + dc] = v
        for dr, dc, v in s0:
            out[br[1][0] + dr][bc[j][0] + dc] = v
    return out