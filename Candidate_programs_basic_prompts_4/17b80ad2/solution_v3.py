def solve(grid):
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    for c in range(w):
        if grid[-1][c] == 0:
            continue
        rows = [i for i in range(h) if grid[i][c] != 0]
        if not rows:
            continue
        vals = [grid[i][c] for i in rows]
        r0 = rows[0]
        v0 = vals[0]
        for r in range(0, r0+1):
            out[r][c] = v0
        for j in range(1, len(rows)):
            r_prev = rows[j-1]
            r_cur = rows[j]
            v_cur = vals[j]
            for r in range(r_prev+1, r_cur+1):
                out[r][c] = v_cur
    return out