def solve(grid):
    h=len(grid); w=len(grid[0])
    zr=[r for r in range(h) for c in range(w) if grid[r][c]==0]
    if not zr: return []
    r0=min(zr); r1=max(zr)
    zc=[c for r in range(h) for c in range(w) if grid[r][c]==0]
    c0=min(zc); c1=max(zc)
    zh=r1-r0+1; zw=c1-c0+1
    # detect vertical or horizontal cut
    if zh and all(grid[r][c0]!=0 for r in range(r0-1,-1,-1) for c in [c0]):
        # vertical: extract above
        start=r0-zh
        if start>0:
            out_h=start
            rows=[start-i for i in range(out_h)]
        else:
            out_h=zh
            rows=[r0-1-i for i in range(out_h)]
        cols=list(range(c0,c0+zw))
    else:
        # horizontal: extract left
        start=c0-zw
        if start>0:
            out_w=start
            cols=[start-i for i in range(out_w)]
        else:
            out_w=zw
            cols=[c0-1-i for i in range(out_w)]
        rows=list(range(r0,r0+zh))
    return [[grid[r][c] for c in cols] for r in rows]