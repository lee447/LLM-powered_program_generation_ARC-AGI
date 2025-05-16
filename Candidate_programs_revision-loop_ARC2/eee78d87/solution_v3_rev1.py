import numpy as np
from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    g = np.array(grid)
    n = g.shape[0]
    c = next(int(v) for v in g.flatten() if v not in (0,7))
    pts = {(i,j) for i in range(n) for j in range(n) if g[i,j]==c}
    for i,j in pts:
        if sum((i+di,j+dj) in pts for di,dj in ((1,0),(-1,0),(0,1),(0,-1)))==4:
            is_x = False
            break
        if sum((i+di,j+dj) in pts for di,dj in ((1,1),(1,-1),(-1,1),(-1,-1)))==4:
            is_x = True
            break
    inner = g[1:-1,1:-1]
    m = inner.shape[0]
    ts = m
    R = m*ts
    out = np.zeros((R,R), int)
    for bi in range(m):
        for bj in range(m):
            col = inner[bi,bj]
            o = (bi+ bj) % 2
            for di in range(ts):
                for dj in range(ts):
                    if is_x:
                        in0 = (di==dj or di+dj==ts-1)
                        in1 = (1<=di<ts-1 and 1<=dj<ts-1)
                    else:
                        in0 = (1<=di<ts-1 and 1<=dj<ts-1)
                        in1 = (di==dj or di+dj==ts-1)
                    if o==0:
                        pick = in0
                    else:
                        pick = in1
                    i = bi*ts+di
                    j = bj*ts+dj
                    if col==7:
                        out[i,j] = 7 if pick else 0
                    else:
                        out[i,j] = 9 if pick else 7
    return out.tolist()