import numpy as np
def solve(grid):
    h=len(grid); w=len(grid[0])
    out=[row[:] for row in grid]
    stripes={}
    for r in range(h):
        c=grid[r][2]
        if c not in (6,7):
            stripes.setdefault(c,[]).append(r)
    for c,rs in stripes.items():
        if len(rs)==2:
            r1,r2=sorted(rs)
            if r2-r1==2:
                rb,r_ref=r1+1,r1
            else:
                rb,r_ref=r2+1,r2
            if 0<=rb<h:
                out[rb][0]=7
                row_ref=grid[r_ref]
                c_max=max(i for i,v in enumerate(row_ref) if v==c)
                if c_max+2<w and out[rb][c_max+2]==7:
                    out[rb][c_max+2]=6
                elif c_max+1<w and out[rb][c_max+1]==7:
                    out[rb][c_max+1]=6
    for c,rs in stripes.items():
        if len(rs)==1:
            r=rs[0]
            if r==h-1:
                row=grid[r]
                c_max=max(i for i,v in enumerate(row) if v==c)
                if c_max+1<w and out[r][c_max+1]==7:
                    out[r][c_max+1]=6
                elif c_max+2<w and out[r][c_max+2]==7:
                    out[r][c_max+2]=6
    return out