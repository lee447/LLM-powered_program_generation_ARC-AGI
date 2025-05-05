def solve(grid):
    R=len(grid); C=len(grid[0])
    blue=[(r,c) for r in range(R) for c in range(C) if grid[r][c]==1]
    nonb=[(r,c,grid[r][c]) for r in range(R) for c in range(C) if grid[r][c]!=0 and grid[r][c]!=1]
    rows=set(r for r,_ in blue)
    inside=[t for t in nonb if t[0] in rows]
    outside=[t for t in nonb if t[0] not in rows]
    if len(inside)==1 and len(outside)==1:
        ar1,ac1,v1=inside[0]
        ar2,ac2,v2=outside[0]
    else:
        ar1,ac1,v1=inside[0]
        ar2,ac2,v2=outside[0]
    orig=[row[:] for row in grid]
    out=[row[:] for row in grid]
    # first copy
    for br,bc in blue:
        dx=ac1-bc
        ok=True
        for r,c in blue:
            nc=c+dx
            if not(0<=nc<C): ok=False; break
            if not(orig[r][nc]==0 or (r,nc)==(ar1,ac1)): ok=False; break
        if ok:
            for r,c in blue:
                nc=c+dx
                out[r][nc]=v1
            break
    # second copy
    for br,bc in blue:
        dy=ar2-br
        ok=True
        for r,c in blue:
            nr=r+dy
            if not(0<=nr<R): ok=False; break
            if not(orig[nr][c]==0 or (nr,c)==(ar2,ac2)): ok=False; break
        if ok:
            for r,c in blue:
                nr=r+dy
                out[nr][c]=v2
            break
    return out