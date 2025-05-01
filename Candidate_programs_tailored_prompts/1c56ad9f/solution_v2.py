def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [[0]*w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if grid[r][c]:
                out[r][c] = grid[r][c]
    for color in set(v for row in grid for v in row if v):
        rows = {}
        for r in range(h):
            cols = [c for c in range(w) if grid[r][c]==color]
            if cols:
                rows[r] = cols
        min_count = min(len(cols) for cols in rows.values())
        stripe_rows = sorted(r for r,cols in rows.items() if len(cols)>min_count)
        if not stripe_rows: continue
        base = stripe_rows[0]
        for r, cols in rows.items():
            if r in stripe_rows: continue
            m0 = (r - base) % 4
            if m0==1: delta = -1
            elif m0==3: delta = 1
            else: delta = 0
            for c in cols:
                if 0 <= c+delta < w:
                    out[r][c] = 0
                    out[r][c+delta] = color
    return out