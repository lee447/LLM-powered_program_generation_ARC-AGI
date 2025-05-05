def solve(grid):
    h = len(grid)
    band = h // 3
    out = []
    for b in range(3):
        cells = []
        for r in range(b * band, (b + 1) * band):
            for c, v in enumerate(grid[r]):
                if v:
                    cells.append((c, v))
        cells.sort(key=lambda x: x[0])
        out.append([v for _, v in cells])
    return out