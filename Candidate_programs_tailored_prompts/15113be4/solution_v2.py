def solve(grid):
    R, C = len(grid), len(grid[0])
    DIV = 4
    full_rows = [i for i in range(R) if all(grid[i][j] == DIV for j in range(C))]
    full_cols = [j for j in range(C) if all(grid[i][j] == DIV for i in range(R))]
    anchor_rows = [0] + [r + 1 for r in full_rows if r + 1 < R]
    anchor_cols = [0] + [c + 1 for c in full_cols if c + 1 < C]
    # detect X in top-left zone
    x_val = None
    ar0, ac0 = anchor_rows[0], anchor_cols[0]
    for i in range(ar0, R):
        for j in range(ac0, C):
            v = grid[i][j]
            if v not in (0, 1, DIV):
                x_val = v
                break
        if x_val is not None:
            break
    # collect offsets of X in top-left zone
    offsets = []
    for i in range(ar0, R):
        for j in range(ac0, C):
            if grid[i][j] == x_val:
                offsets.append((i - ar0, j - ac0))
    # recolor matching blue cells in each diagonal zone
    for k in range(1, min(len(anchor_rows), len(anchor_cols))):
        ar, ac = anchor_rows[k], anchor_cols[k]
        for dr, dc in offsets:
            r, c = ar + dr, ac + dc
            if 0 <= r < R and 0 <= c < C and grid[r][c] == 1:
                grid[r][c] = x_val
    return grid