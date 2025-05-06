def solve(grid):
    R, C = len(grid), len(grid[0])
    sep = 4
    from collections import Counter
    cnt = Counter(c for row in grid for c in row)
    newc = max((c for c in cnt if c not in (0,1,sep)), key=lambda c: cnt[c], default=None)
    # find separator rows/cols
    sep_rows = [i for i in range(R) if all(grid[i][j]==sep for j in range(C))]
    sep_cols = [j for j in range(C) if all(grid[i][j]==sep for i in range(R))]
    # compute blocks
    rb = []
    prev = -1
    for sr in sep_rows + [R]:
        if sr - prev > 1:
            rb.append((prev+1, sr-1))
        prev = sr
    cb = []
    prev = -1
    for sc in sep_cols + [C]:
        if sc - prev > 1:
            cb.append((prev+1, sc-1))
        prev = sc
    g = [row[:] for row in grid]
    for (r0,r1) in rb:
        h = r1-r0+1
        for (c0,c1) in cb:
            w = c1-c0+1
            # collect shapeColor positions
            pts = [(i,j) for i in range(r0,r1+1) for j in range(c0,c1+1) if grid[i][j]==1]
            if not pts: continue
            if h==3 and w==3:
                for i in range(3):
                    ii = r0+i; jj = c0+2-i
                    if grid[ii][jj]==1:
                        g[ii][jj] = newc
            elif h>3 and w<=h:
                mid = (h-1)//2 + (1 if h>3 else 0)
                ri = r0+mid
                for cj in (c0, c1):
                    if grid[ri][cj]==1:
                        g[ri][cj] = newc
    return g