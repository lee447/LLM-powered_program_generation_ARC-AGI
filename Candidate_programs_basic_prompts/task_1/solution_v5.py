def solve(grid):
    R, C = len(grid), len(grid[0])
    row_counts = [sum(1 for v in row if v != 0) for row in grid]
    max_r = max(row_counts)
    thr_r = (max_r + 1) // 2
    pos_r = [i for i, c in enumerate(row_counts) if c >= thr_r]
    runs_r, cur = [], []
    for i in sorted(pos_r):
        if cur and i != cur[-1] + 1:
            runs_r.append(cur); cur = []
        cur.append(i)
    if cur: runs_r.append(cur)
    h = len(runs_r[0])
    shift_v = runs_r[0][0]
    second_v = runs_r[1][0] if len(runs_r) > 1 else shift_v + h
    period_v = second_v - shift_v
    col_counts = [sum(1 for r in range(R) if grid[r][c] != 0) for c in range(C)]
    max_c = max(col_counts)
    thr_c = (max_c + 1) // 2
    pos_c = [j for j, c in enumerate(col_counts) if c >= thr_c]
    runs_c, cur = [], []
    for j in sorted(pos_c):
        if cur and j != cur[-1] + 1:
            runs_c.append(cur); cur = []
        cur.append(j)
    if cur: runs_c.append(cur)
    w = len(runs_c[0])
    shift_h = runs_c[0][0]
    second_h = runs_c[1][0] if len(runs_c) > 1 else shift_h + w
    period_h = second_h - shift_h
    out = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            v = grid[r][c]
            if v != 0 and (r - shift_v) % period_v < h and (c - shift_h) % period_h < w:
                out[r][c] = v
    return out