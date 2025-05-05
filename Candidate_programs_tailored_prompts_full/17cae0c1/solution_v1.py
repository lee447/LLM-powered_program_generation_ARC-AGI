def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    zone_w = cols // 3
    counts = []
    for z in range(3):
        start = z * zone_w
        cnt = 0
        for r in range(rows):
            for c in range(start, start + zone_w):
                if grid[r][c] == 5:
                    cnt += 1
        counts.append(cnt)
    palette = sorted({grid[r][c] for r in range(rows) for c in range(cols) if grid[r][c] not in (0, 5)})
    ranks = sorted(range(3), key=lambda z: counts[z], reverse=True)
    cmap = {z: palette[i] for i, z in enumerate(ranks)}
    out = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            z = c // zone_w
            out[r][c] = cmap[z]
    return out