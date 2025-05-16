def solve(grid):
    bg = max({c: sum(row.count(c) for row in grid) for row in grid for c in set(row)}.items(), key=lambda x: x[1])[0]
    coords = {}
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c != bg:
                coords.setdefault(c, []).append(y)
    items = sorted(((c, ys) for c, ys in coords.items()), key=lambda x: min(x[1]))
    res = []
    for c, ys in items:
        for _ in ys:
            res.append([c])
    return res