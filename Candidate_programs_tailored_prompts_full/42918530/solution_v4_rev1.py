def solve(grid):
    g = [row[:] for row in grid]
    R, C = len(g), len(g[0])
    zero_rows = [r for r in range(R) if all(v == 0 for v in g[r])]
    row_bands = [(zero_rows[i]+1, zero_rows[i+1]-1) for i in range(len(zero_rows)-1) if zero_rows[i]+1 <= zero_rows[i+1]-1]
    zero_cols = [c for c in range(C) if all(g[r][c] == 0 for r in range(R))]
    col_bands = [(zero_cols[i]+1, zero_cols[i+1]-1) for i in range(len(zero_cols)-1) if zero_cols[i]+1 <= zero_cols[i+1]-1]
    n = len(row_bands)
    mid = n // 2
    for i, (r0, r1) in enumerate(row_bands):
        if i != mid: continue
        for j, (c0, c1) in enumerate(col_bands):
            if j > i: continue
            color = g[r0][c0]
            for d in range(r1-r0+1):
                if 0 <= r0+d < R and 0 <= c0+d < C:
                    g[r0+d][c0+d] = color
                if 0 <= r0+d < R and 0 <= c1-d < C:
                    g[r0+d][c1-d] = color
    return g