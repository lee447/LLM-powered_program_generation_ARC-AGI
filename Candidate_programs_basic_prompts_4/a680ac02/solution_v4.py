def solve(grid):
    regions = []
    h = len(grid)
    w = len(grid[0])
    for color in range(1, 10):
        coords = [(y, x) for y in range(h) for x in range(w) if grid[y][x] == color]
        if not coords:
            continue
        ys = [y for y, x in coords]
        xs = [x for y, x in coords]
        miny, maxy = min(ys), max(ys)
        minx, maxx = min(xs), max(xs)
        dh = maxy - miny + 1
        dw = maxx - minx + 1
        if dh == dw:
            D = dh
            cnt = len(coords)
            if cnt == 4*D - 4:
                regions.append((minx, miny, D, color, set(coords)))
    regions.sort(key=lambda r: r[0])
    if not regions:
        return []
    D = regions[0][2]
    out = [[0]* (D * len(regions)) for _ in range(D)]
    for i, (minx, miny, D, color, cells) in enumerate(regions):
        for dy in range(D):
            for dx in range(D):
                if (miny+dy, minx+dx) in cells:
                    out[dy][i*D+dx] = color
    return out