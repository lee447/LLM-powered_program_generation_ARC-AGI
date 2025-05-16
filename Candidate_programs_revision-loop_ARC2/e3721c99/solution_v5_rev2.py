from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h,w=len(grid),len(grid[0])
    pattern_end=next((i for i in range(1,h) if all(v==0 for v in grid[i])),h)
    shape_start=next((i for i in range(h) if any(v==5 for v in grid[i])),h)
    blocks={}
    for r in range(pattern_end):
        for c in range(w):
            v=grid[r][c]
            if v not in (0,5):
                if v not in blocks:
                    blocks[v]=[r,r,c,c]
                else:
                    b=blocks[v]
                    b[0]=min(b[0],r);b[1]=max(b[1],r)
                    b[2]=min(b[2],c);b[3]=max(b[3],c)
    bl=[]
    for v,(r0,r1,c0,c1) in blocks.items():
        h0,cw=c1-c0+1,r1-r0+1
        bl.append((v,cw,h0,r0,c0))
    bl.sort(key=lambda x: x[4])
    res=[row[:] for row in grid]
    for r in range(shape_start,h):
        for c in range(w):
            if grid[r][c]==5:
                best=None;bd=None
                for v,h0,w0,r0,c0 in bl:
                    dr=r-(shape_start)
                    dc=c-(c0)
                    k=int(round(dr/w0))
                    m=int(round(dc/h0))
                    cr=r0+w0//2
                    cc=c0+h0//2
                    dr2=r-(cr+k*w0)
                    dc2=c-(cc+m*h0)
                    d=dr2*dr2+dc2*dc2
                    if bd is None or d<bd:
                        bd=d;best=(v,h0,w0,r0,c0)
                v,h0,w0,r0,c0=best
                rr=(r-r0)%w0;cc2=(c-c0)%h0
                res[r][c]=v if grid[r0+rr][c0+cc2]==v else 0
    return res