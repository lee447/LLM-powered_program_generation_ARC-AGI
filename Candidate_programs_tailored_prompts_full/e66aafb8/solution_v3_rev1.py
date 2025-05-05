def solve(grid):
    h, w = len(grid), len(grid[0])
    g = [row[1:w-1] for row in grid[1:h-1]]
    zs = [(i, j) for i, row in enumerate(g) for j, v in enumerate(row) if v == 0]
    rows = [i for i, _ in zs]
    cols = [j for _, j in zs]
    r0, r1 = min(rows), max(rows)
    c0, c1 = min(cols), max(cols)
    h0 = r1 - r0 + 1
    out = [g[i][c0:c1+1] for i in range(r0 - h0, r0)]
    return out[::-1]