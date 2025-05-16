import numpy as np
from itertools import accumulate
def solve(grid):
    H,W=len(grid),len(grid[0])
    w_segs=[];cur=grid[0][0];cnt=0
    for x in grid[0]:
        if x==cur:cnt+=1
        else:
            w_segs.append(cnt);cur=x;cnt=1
    w_segs.append(cnt)
    h_segs=[];cur=grid[0][0];cnt=0
    for r in range(H):
        x=grid[r][0]
        if x==cur:cnt+=1
        else:
            h_segs.append(cnt);cur=x;cnt=1
    h_segs.append(cnt)
    w_starts=[0]+list(accumulate(w_segs))[:-1]
    h_starts=[0]+list(accumulate(h_segs))[:-1]
    HB,WB=len(h_segs),len(w_segs)
    macro=[[grid[h_starts[i]][w_starts[j]] for j in range(WB)] for i in range(HB)]
    outH=sum(w_segs);outW=sum(h_segs)
    out=[[0]*outW for _ in range(outH)]
    for i in range(WB):
        for j in range(HB):
            col=macro[j][i]
            r0=sum(w_segs[:i]);c0=sum(h_segs[:j])
            for dr in range(w_segs[i]):
                for dc in range(h_segs[j]):
                    out[r0+dr][c0+dc]=col
    return out