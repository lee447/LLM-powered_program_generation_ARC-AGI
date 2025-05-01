def solve(grid):
    H, W = len(grid), len(grid[0])
    out = [[0]*W for _ in range(H)]
    colors = set(cell for row in grid for cell in row if cell)
    for c in colors:
        coords = [(r, x) for r, row in enumerate(grid) for x, v in enumerate(row) if v==c]
        rows = {}
        for r, x in coords:
            rows.setdefault(r, []).append(x)
        stripe_rows = sorted(r for r, xs in rows.items() if max(xs)-min(xs)>=2)
        bar_cols = sorted({x for r, xs in rows.items() if r not in stripe_rows for x in xs})
        center = (bar_cols[0] + bar_cols[-1])//2
        for r in stripe_rows:
            for x in rows[r]:
                out[r][x] = c
        for i in range(len(stripe_rows)-1):
            top, bot = stripe_rows[i], stripe_rows[i+1]
            direction = -1 if i%2==0 else 1
            for j,r in enumerate(range(top+1, bot)):
                if j%2==0:
                    for x in bar_cols:
                        nx = x + direction
                        if 0<=nx<W:
                            out[r][nx] = c
                else:
                    for x in bar_cols:
                        out[r][x] = c
    return out