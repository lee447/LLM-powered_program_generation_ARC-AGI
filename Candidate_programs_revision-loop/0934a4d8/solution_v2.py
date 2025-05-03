def solve(grid):
    R=len(grid);C=len(grid[0])
    pts=[(r,c) for r in range(R) for c in range(C) if grid[r][c]==8]
    if not pts:return grid
    rs=[r for r,c in pts];cs=[c for r,c in pts]
    r0,r1=min(rs),max(rs);c0,c1=min(cs),max(cs)
    h,w=r1-r0+1,c1-c0+1
    import math
    acx=(r0+r1)/2;acy=(c0+c1)/2
    patches=[]
    for r in range(R-h+1):
        for c in range(C-w+1):
            if any(grid[r+i][c+j]==8 for i in range(h) for j in range(w)):continue
            v=grid[r][c]
            if v==0:continue
            ok=True
            for i in range(h):
                for j in range(w):
                    if grid[r+i][c+j]!=v:
                        ok=False;break
                if not ok:break
            if ok:
                cx=r+h/2;cy=c+w/2
                ang=math.atan2(cx-acx,cy-acy)
                patches.append((ang,r,c))
    patches.sort()
    out=[[0]*w for _ in range(h)]
    for _,r,c in patches:
        for i in range(h):
            for j in range(w):
                out[i][j]=grid[r+i][c+j]
    return out