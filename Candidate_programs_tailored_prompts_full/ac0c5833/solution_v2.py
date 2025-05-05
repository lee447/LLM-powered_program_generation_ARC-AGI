def solve(grid):
    rows=len(grid); cols=len(grid[0])
    anchors_r=sorted({r for r in range(rows) for c in range(cols) if grid[r][c]==4})
    anchors_c=sorted({c for r in range(rows) for c in range(cols) if grid[r][c]==4})
    reds=[(r,c) for r in range(rows) for c in range(cols) if grid[r][c]==2]
    origins=[(r,c) for r,c in reds if (r==0 or grid[r-1][c]!=2) and (c==0 or grid[r][c-1]!=2)]
    if not origins:
        return grid
    r0,c0=origins[0]
    base_r=max(r for r in anchors_r if r<=r0)
    base_c=max(c for c in anchors_c if c<=c0)
    pattern=[(r-r0,c-c0) for r,c in reds]
    h=max(dr for dr,dc in pattern)+1; w=max(dc for dr,dc in pattern)+1
    next_r={a:None for a in anchors_r}
    for i,a in enumerate(anchors_r[:-1]): next_r[a]=anchors_r[i+1]
    next_c={a:None for a in anchors_c}
    for i,a in enumerate(anchors_c[:-1]): next_c[a]=anchors_c[i+1]
    out=[row[:] for row in grid]
    for ar in anchors_r:
        nr=next_r.get(ar)
        if nr is None or nr-ar< h: continue
        for ac in anchors_c:
            nc=next_c.get(ac)
            if nc is None or nc-ac< w: continue
            for dr,dc in pattern:
                r,c=ar+dr,ac+dc
                if 0<=r<rows and 0<=c<cols and out[r][c]==0:
                    out[r][c]=2
    return out