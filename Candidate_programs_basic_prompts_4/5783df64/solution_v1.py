def solve(grid):
    h = len(grid)
    s = h // 3
    out = []
    for i in range(3):
        elems = []
        for r in range(i * s, (i + 1) * s):
            for c, v in enumerate(grid[r]):
                if v:
                    elems.append((c, v))
        elems.sort(key=lambda x: x[0])
        out.append([v for _, v in elems])
    return out