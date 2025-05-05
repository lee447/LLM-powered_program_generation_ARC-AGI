def solve(grid):
    h = len(grid)
    w = len(grid[0])
    bg = grid[0][0]
    colors = {grid[r][c] for r in range(h) for c in range(w) if grid[r][c] != bg}
    bands = []
    for v in colors:
        rows = [r for r in range(h) if any(grid[r][c] == v for c in range(w))]
        if rows:
            bands.append((min(rows), v, rows))
    bands.sort(key=lambda x: x[0])
    out = [[bg] * w for _ in range(h)]
    for i, (_, v, rows) in enumerate(bands):
        d = -1 if i % 2 == 0 else 1
        for r in rows:
            for c in range(w):
                if grid[r][c] == v:
                    out[r][c + d] = v
    return out