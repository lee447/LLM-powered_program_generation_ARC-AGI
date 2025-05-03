import collections
from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h,w = len(grid),len(grid[0])
    nonzero_rows = sorted({r for r in range(h) for c in range(w) if grid[r][c]!=0})
    bands=[]
    if nonzero_rows:
        start=prev=nonzero_rows[0]
        for r in nonzero_rows[1:]:
            if r>prev+1:
                bands.append((start,prev))
                start=r
            prev=r
        bands.append((start,prev))
    out=[[0]*w for _ in range(h)]
    for rs,re in bands:
        hb = re-rs+1
        cols = sorted({c for r in range(rs,re+1) for c in range(w) if grid[r][c]!=0})
        if not cols: continue
        segments=[]; seg=[cols[0]]
        for c in cols[1:]:
            if c>seg[-1]+1:
                segments.append((seg[0],seg[-1])); seg=[c]
            else:
                seg.append(c)
        segments.append((seg[0],seg[-1]))
        widths = [ce-cs+1 for cs,ce in segments]
        freq=collections.Counter(widths)
        template_w = max(freq, key=lambda x:(freq[x],x))
        if template_w<=1: continue
        build_segs = [cs for cs,ce in segments if ce-cs+1>=template_w]
        counts = [[{} for _ in range(template_w)] for _ in range(hb)]
        for cs in build_segs:
            for dr in range(hb):
                for dc in range(template_w):
                    val = grid[rs+dr][cs+dc]
                    if val!=0:
                        d=counts[dr][dc]
                        d[val]=d.get(val,0)+1
        template=[[0]*template_w for _ in range(hb)]
        for dr in range(hb):
            for dc in range(template_w):
                d=counts[dr][dc]
                if d:
                    template[dr][dc]=max(d, key=lambda x:(d[x],x))
        for cs,ce in segments:
            if ce-cs+1>=template_w:
                for dr in range(hb):
                    for dc in range(template_w):
                        out[rs+dr][cs+dc]=template[dr][dc]
    return out