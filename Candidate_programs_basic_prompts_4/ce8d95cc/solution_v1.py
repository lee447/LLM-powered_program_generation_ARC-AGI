def solve(grid):
    R, C = len(grid), len(grid[0])
    cols = []
    for c in range(C):
        s = {grid[r][c] for r in range(R)}
        if len(s) == 1:
            cols.append(c)
    from collections import Counter
    cnt = Counter()
    for row in grid:
        cnt.update(row)
    background = cnt.most_common(1)[0][0]
    rows = []
    stripe_cols = set(cols)
    for r in range(R):
        vals = [grid[r][c] for c in range(C) if c not in stripe_cols]
        if vals and all(v == vals[0] for v in vals) and vals[0] != background:
            rows.append(r)
    def windows(indices, limit):
        w = []
        for i,x in enumerate(indices):
            if i == 0:
                w += [x-1, x, x+1]
            else:
                w += [x, x+1]
        res = []
        seen = set()
        for v in w:
            if 0 <= v < limit and v not in seen:
                seen.add(v)
                res.append(v)
        return res
    wcols = windows(cols, C)
    wrows = windows(rows, R)
    return [[grid[r][c] for c in wcols] for r in wrows]