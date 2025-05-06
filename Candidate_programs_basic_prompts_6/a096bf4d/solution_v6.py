from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R = len(grid)
    C = len(grid[0]) if R else 0
    zr = [i for i,row in enumerate(grid) if all(v==0 for v in row)]
    zc = [j for j in range(C) if all(grid[i][j]==0 for i in range(R))]
    br = []
    for a,b in zip(zr, zr[1:]):
        if b>a+1: br.append((a+1, b-1))
    bc = []
    for a,b in zip(zc, zc[1:]):
        if b>a+1: bc.append((a+1, b-1))
    out = [row[:] for row in grid]
    for (r0,r1) in br:
        dr = (r1 - r0 + 1)//2
        # reference block in this row
        cref = None
        pref = None
        # find first block with an irregular
        for (c0,c1) in bc:
            # interior 2x2
            i1,j1 = r0+dr-1, c0+dr-1
            vals = [
                grid[i1][j1+1],
                grid[i1+1][j1],
                grid[i1+1][j1+1]
            ]
            # mode is shape
            from collections import Counter
            cnt = Counter(vals)
            shape,_ = max(cnt.items(), key=lambda x:(x[1],x[0]))
            for k,v in enumerate(vals, start=1):
                if v!=shape:
                    cref = v
                    pref = k
                    break
            if pref is not None:
                break
        if pref is None:
            continue
        for (c0,c1) in bc:
            i1,j1 = r0+dr-1, c0+dr-1
            # position to set
            if pref==1:
                rr,cc = i1, j1+1
            elif pref==2:
                rr,cc = i1+1, j1
            else:
                rr,cc = i1+1, j1+1
            if grid[rr][cc] == shape:
                out[rr][cc] = cref
    return out