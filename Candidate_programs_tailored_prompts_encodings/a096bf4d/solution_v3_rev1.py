def solve(grid):
    R, C = len(grid), len(grid[0])
    sep_rows = {r for r in range(R) if all(v == 0 for v in grid[r])}
    sep_cols = {c for c in range(C) if all(grid[r][c] == 0 for r in range(R))}
    row_segs = []
    r = 0
    while r < R:
        if r in sep_rows:
            r += 1
        else:
            start = r
            while r < R and r not in sep_rows:
                r += 1
            row_segs.append((start, r))
    col_segs = []
    c = 0
    while c < C:
        if c in sep_cols:
            c += 1
        else:
            start = c
            while c < C and c not in sep_cols:
                c += 1
            col_segs.append((start, c))
    r0, r1 = row_segs[0]
    c0, c1 = col_segs[0]
    bg1 = grid[r0][c0]
    shape_global = [(i, j) for i in range(r0, r1) for j in range(c0, c1) if grid[i][j] != bg1 and grid[i][j] != 0]
    shape_local = [(i - r0, j - c0) for i, j in shape_global]
    S = set(shape_local)
    def deg(p):
        i, j = p
        return sum((i + di, j + dj) in S for di, dj in ((1,0),(-1,0),(0,1),(0,-1)))
    pivot_local = max(shape_local, key=lambda p: (deg(p), p[0], -p[1]))
    pivot_color = grid[r0 + pivot_local[0]][c0 + pivot_local[1]]
    rl0, rl1 = row_segs[0]
    cl0, cl1 = col_segs[-1]
    bg_last = grid[rl0][cl0]
    arms_color = None
    for i in range(rl0, rl1):
        for j in range(cl0, cl1):
            if grid[i][j] != bg_last and grid[i][j] != 0:
                arms_color = grid[i][j]
                break
        if arms_color is not None:
            break
    for rr0, rr1 in row_segs:
        for cc0, cc1 in col_segs:
            for lr, lc in shape_local:
                i, j = rr0 + lr, cc0 + lc
                grid[i][j] = pivot_color if (lr, lc) == pivot_local else arms_color
    return grid