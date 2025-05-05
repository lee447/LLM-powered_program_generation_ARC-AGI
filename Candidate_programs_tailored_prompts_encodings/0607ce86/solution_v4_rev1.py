from typing import List
def solve(grid: List[List[int]])->List[List[int]]:
    h,w=len(grid),len(grid[0])
    nonv=[sum(1 for v in row if v not in (0,3)) for row in grid]
    mx=max(nonv)
    thr=mx/2
    seg_rows=[i for i,c in enumerate(nonv) if c>=thr]
    segments=[]
    i=0
    while i<len(seg_rows):
        s=seg_rows[i]; j=i
        while j+1<len(seg_rows) and seg_rows[j+1]==seg_rows[j]+1: j+=1
        segments.append((seg_rows[i],seg_rows[j])); i=j+1
    ps,pe=segments[0]
    ph=pe-ps+1
    starts=[s for s,e in segments if e-s+1==ph]
    k=len(starts)
    cleaned=[[0]*w for _ in range(ph)]
    for dr in range(ph):
        for j in range(w):
            vals=[grid[s+dr][j] for s in starts]
            cands=set(vals)-{0,3}
            if len(cands)==1:
                cleaned[dr][j]=cands.pop()
            else:
                if not cands:
                    cleaned[dr][j]=3 if all(v==3 for v in vals) else 0
                else:
                    cleaned[dr][j]=next(iter(cands))
    out=[[0]*w for _ in range(h)]
    for s in starts:
        for dr in range(ph):
            out[s+dr]=cleaned[dr][:]
    return out