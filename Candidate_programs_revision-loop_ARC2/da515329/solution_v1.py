def solve(grid):
    h=len(grid);w=len(grid[0])
    out=[[0]*w for _ in range(h)]
    pts=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==8]
    if not pts: return out
    for r,c in pts: out[r][c]=8
    rs=[r for r,c in pts]; cs=[c for r,c in pts]
    minr,maxr=min(rs),max(rs); minc,maxc=min(cs),max(cs)
    mid_r=(minr+maxr)/2; mid_c=(minc+maxc)/2
    corners=[(minr,minc),(minr,maxc),(maxr,minc),(maxr,maxc)]
    for r0,c0 in corners:
        sign_r=1 if r0>mid_r else -1
        sign_c=1 if c0>mid_c else -1
        dr,dc=sign_r,sign_c
        k=1
        while True:
            r=r0+dr*k; c=c0+dc*k
            if r<0 or r>=h or c<0 or c>=w: break
            if k%2==1: out[r][c]=8
            k+=1
    return out