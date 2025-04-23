def solve(grid):
    n, m = len(grid), len(grid[0])
    cnt8 = sum(1 for row in grid for cell in row if cell == 8)
    anchor = 8 if cnt8 > 0 else 9
    rows = [i for i, row in enumerate(grid) for j, v in enumerate(row) if v == anchor]
    cols = [j for i, row in enumerate(grid) for j, v in enumerate(row) if v == anchor]
    r0, r1 = min(rows), max(rows)
    c0, c1 = min(cols), max(cols)
    h, w = r1 - r0 + 1, c1 - c0 + 1
    noise = {6, 7}
    nl = nr = float('inf')
    if c0 >= w:
        nl = sum(1 for i in range(r0, r1+1) for j in range(c0-w, c0) if grid[i][j] in noise)
    if c1 + w < m:
        nr = sum(1 for i in range(r0, r1+1) for j in range(c1+1, c1+1+w) if grid[i][j] in noise)
    if nl <= nr:
        sc = c0 - w
    else:
        sc = c1 + 1
    return [grid[i][sc:sc+w] for i in range(r0, r1+1)]