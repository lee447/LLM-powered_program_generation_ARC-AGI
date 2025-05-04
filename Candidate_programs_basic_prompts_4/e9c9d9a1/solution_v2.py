def solve(grid):
    n_rows = len(grid)
    n_cols = len(grid[0])
    row_seps = [i for i in range(n_rows) if all(grid[i][j] == 3 for j in range(n_cols))]
    col_seps = [j for j in range(n_cols) if all(grid[i][j] == 3 for i in range(n_rows))]
    row_seps.sort()
    col_seps.sort()
    blocks_rows = []
    prev = 0
    for r in row_seps:
        if prev <= r - 1:
            blocks_rows.append((prev, r - 1))
        prev = r + 1
    if prev <= n_rows - 1:
        blocks_rows.append((prev, n_rows - 1))
    blocks_cols = []
    prev = 0
    for c in col_seps:
        if prev <= c - 1:
            blocks_cols.append((prev, c - 1))
        prev = c + 1
    if prev <= n_cols - 1:
        blocks_cols.append((prev, n_cols - 1))
    R = len(blocks_rows)
    C = len(blocks_cols)
    out = [row[:] for row in grid]
    for bi, (r0, r1) in enumerate(blocks_rows):
        for bj, (c0, c1) in enumerate(blocks_cols):
            if bj == 0 and bi == 0:
                color = 2
            elif bj == 0 and bi == R - 1:
                color = 1
            elif bj == C - 1 and bi == 0:
                color = 4
            elif bj == C - 1 and bi == R - 1:
                color = 8
            elif 1 <= bj <= C - 2 and 1 <= bi <= R - 2:
                color = 7
            else:
                continue
            for i in range(r0, r1 + 1):
                for j in range(c0, c1 + 1):
                    out[i][j] = color
    return out