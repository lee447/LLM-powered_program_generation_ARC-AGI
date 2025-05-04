def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = 0
    stripe_rows = sorted(i for i in range(h) if len(set(grid[i])) == 1 and grid[i][0] != bg)
    stripe_cols = sorted(j for j in range(w) if len({grid[i][j] for i in range(h)}) == 1 and grid[0][j] != bg)
    row_ranges = [(stripe_rows[i]+1, stripe_rows[i+1]) for i in range(len(stripe_rows)-1)]
    col_ranges = [(stripe_cols[i]+1, stripe_cols[i+1]) for i in range(len(stripe_cols)-1)]
    out = [row[:] for row in grid]
    for br in range(len(row_ranges)):
        r0, r1 = row_ranges[br]
        rows = range(r0, r1)
        for ci in range(len(col_ranges)-1):
            c0, c1 = col_ranges[ci]
            c2, c3 = col_ranges[ci+1]
            shape = []
            color = None
            for r in rows:
                for c in range(c0, c1):
                    v = grid[r][c]
                    if v != bg:
                        shape.append((r-r0, c-c0))
                        color = v
            if not shape: continue
            occupied = any(grid[r][c] != bg for r in rows for c in range(c2, c3))
            if occupied: continue
            for dr, dc in shape:
                out[r0+dr][c2+dc] = color
    return out