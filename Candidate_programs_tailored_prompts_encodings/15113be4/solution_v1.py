def solve(grid):
    n, m = len(grid), len(grid[0])
    gl_rows = [i for i in range(n) if sum(1 for v in grid[i] if v == 4) > m//2]
    gl_cols = [j for j in range(m) if sum(1 for i in range(n) if grid[i][j] == 4) > n//2]
    gl_rows.sort()
    gl_cols.sort()
    rsegs = []
    prev = -1
    for r in gl_rows + [n]:
        if r - prev > 1:
            rsegs.append((prev+1, r-1))
        prev = r
    csegs = []
    prev = -1
    for c in gl_cols + [m]:
        if c - prev > 1:
            csegs.append((prev+1, c-1))
        prev = c
    for rs, re in rsegs:
        for cs, ce in csegs:
            pts = [(i, j) for i in range(rs, re+1) for j in range(cs, ce+1) if grid[i][j] not in (0,1,4)]
            if len(pts) != 4:
                continue
            vals = {grid[i][j] for i,j in pts}
            if len(vals) != 1:
                continue
            color = vals.pop()
            # find diagonal endpoints of block with positive slope (main diag)
            ep = None
            for a in range(4):
                for b in range(a+1,4):
                    (r1,c1),(r2,c2) = pts[a], pts[b]
                    if (r2-r1)*(c2-c1) > 0:
                        ep = [(r1,c1),(r2,c2)]
                        break
                if ep:
                    break
            if not ep:
                continue
            cr = (rs + re)//2
            cc = (cs + ce)//2
            for r0,c0 in ep:
                nr = 2*cr - r0
                nc = 2*cc - c0
                if rs <= nr <= re and cs <= nc <= ce and grid[nr][nc] == 1:
                    grid[nr][nc] = color
    return grid