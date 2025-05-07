from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    pts = sorted(((r,c,grid[r][c]) for r in range(H) for c in range(W) if grid[r][c]!=0), key=lambda t:(t[0]+t[1],t[0],t[1]))
    out = [row[:] for row in grid]
    def sign(x): return (x>0)-(x<0)
    if len(pts)==1:
        r,c,v = pts[0]
        mid = (H-1)/2
        rr = int(2*mid-r)
        if 0<=rr<H:
            for rr0 in range(min(r,rr)+1, max(r,rr)):
                out[rr0][c]=5
            out[rr][c]=v
        return out
    for (r0,c0,v0),(r1,c1,v1) in zip(pts,pts[1:]):
        I = (r1, c0)
        dr = sign(r1-r0)
        for rr in range(r0+dr, r1, dr):
            out[rr][c0]=5
        dc = sign(c1-c0)
        for cc in range(c0+dc, c1, dc):
            out[r1][cc]=5
        if 0<=I[0]<H and 0<=I[1]<W:
            if r0!=r1 and c0!=c1:
                out[I[0]][I[1]] = 4
            else:
                out[I[0]][I[1]] = 5
        out[r1][c1]=v1
        out[r0][c0]=v0
        # radiate diagonals
        for (r,c,v,dr,dc) in [(r0,c0,v0,1,-1),(r1,c1,v1,-1,1)]:
            rr,cc = r+dr, c+dc
            while 0<=rr<H and 0<=cc<W:
                out[rr][cc] = 4
                rr+=dr; cc+=dc
    return out