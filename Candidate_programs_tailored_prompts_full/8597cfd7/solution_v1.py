def solve(grid):
    h = len(grid)
    w = len(grid[0])
    band = next(r for r in range(h) if all(grid[r][c] == 5 for c in range(w)))
    stripe_cols = set()
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 0 and v != 5:
                stripe_cols.add(c)
    imbalances = []
    for c in stripe_cols:
        val = next(grid[r][c] for r in range(h) if grid[r][c] not in (0,5))
        above = sum(1 for r in range(band) if grid[r][c] == val)
        below = sum(1 for r in range(band+1, h) if grid[r][c] == val)
        imbalances.append((below - above, val))
    color = max(imbalances, key=lambda x: x[0])[1]
    return [[color, color], [color, color]]