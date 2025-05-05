import numpy as np
def solve(grid):
    h,w=len(grid),len(grid[0])
    res=[[0]*w for _ in range(h)]
    pts=[(r,c) for r in range(h) for c in range(w) if grid[r][c]!=0]
    if not pts: return res
    color=grid[pts[0][0]][pts[0][1]]
    rows=sorted(r for r in range(h) if sum(grid[r][c]==color for c in range(w))>2)
    cols=sorted(c for c in range(w) if sum(grid[r][c]==color for r in range(h))>2)
    n=len(rows)
    cycle=[-1,0,1,0]
    if n<=2:
        stripe_shifts=[0]*n
    else:
        offset=1 if n%4==3 else 0
        stripe_shifts=[cycle[(offset+j)%4] for j in range(n)]
    apply_v=not(n<=2 and len(cols)>2)
    for r,c in pts:
        if r in rows:
            j=rows.index(r)
            shift=stripe_shifts[j]
        else:
            if apply_v:
                i=max(i for i,rr in enumerate(rows) if rr<r)
                d=r-rows[i]-1
                shift=cycle[d%4]
            else:
                shift=0
        nc=c+shift
        res[r][nc]=color
    return res