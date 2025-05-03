def solve(grid):
    h = len(grid)
    w = len(grid[0])
    stripe_rows = [r for r in range(h) if all(grid[r][c] == 4 for c in range(w))]
    stripe_cols = [c for c in range(w) if all(grid[r][c] == 4 for r in range(h))]
    cell_h = stripe_rows[1] - stripe_rows[0] - 1
    cell_w = stripe_cols[1] - stripe_cols[0] - 1
    colors = set()
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v not in (0,1,4):
                colors.add(v)
    highlight = max(colors) if colors else 1
    out = [row[:] for row in grid]
    for bi in range(len(stripe_rows)-1):
        for bj in range(len(stripe_cols)-1):
            r0 = stripe_rows[bi] + 1
            c0 = stripe_cols[bj] + 1
            block = [out[r0+i][c0:c0+cell_w] for i in range(cell_h)]
            if cell_h>=2 and cell_w>=3:
                if block[0][0] == block[0][2] == block[1][1] != 0:
                    for di, dj in ((0,0),(0,2),(1,1)):
                        out[r0+di][c0+dj] = highlight
    return out