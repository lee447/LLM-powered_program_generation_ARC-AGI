from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    pts = [(r,c) for r in range(h) for c in range(w) if grid[r][c]!=0]
    if not pts:
        return grid
    c = grid[pts[0][0]][pts[0][1]]
    alt = 3 if c==6 else 6
    rs = [r for r,_ in pts]; cs = [c_ for _,c_ in pts]
    rmin,rmax,minc,maxc = min(rs),max(rs),min(cs),max(cs)
    ph,pw = rmax-rmin+1, maxc-minc+1
    mask = [[1 if grid[rmin+i][minc+j]==grid[rmin][minc] else 0 for j in range(pw)] for i in range(ph)]
    gc_r, gc_c = (h-1)/2, (w-1)/2
    cc_r, cc_c = (rmin+rmax)/2, (minc+maxc)/2
    def rot(vr,vc):
        return -vc, vr
    out = [row[:] for row in grid]
    for k in range(4):
        angle = k
        vr, vc = cc_r-gc_r, cc_c-gc_c
        for _ in range(k):
            vr,vc = rot(vr,vc)
        new_cc_r, new_cc_c = gc_r+vr, gc_c+vc
        if k%2==0:
            mh,mw = ph,pw
        else:
            mh,mw = pw,ph
        topleft_r = new_cc_r - (mh-1)/2
        topleft_c = new_cc_c - (mw-1)/2
        for i in range(mh):
            for j in range(mw):
                mi,mj = i,j
                if k%2==1:
                    mi,mj = ph-1-j, i
                if mask[mi][mj]:
                    rr = int(round(topleft_r+i))
                    cc2 = int(round(topleft_c+j))
                    if 0<=rr<h and 0<=cc2<w:
                        out[rr][cc2] = c if k%2==0 else alt
    return out