from collections import Counter
def solve(grid):
    h,w=len(grid),len(grid[0])
    rows=[r for r in range(h) if any(grid[r][c]!=0 for c in range(w))]
    bands=[]
    if rows:
        start=prev=rows[0]
        for r in rows[1:]:
            if r>prev+1:
                bands.append((start,prev))
                start=r
            prev=r
        bands.append((start,prev))
    out=[[0]*w for _ in range(h)]
    for rs,re in bands:
        hb=re-rs+1
        cols=[c for c in range(w) if any(grid[r][c]!=0 for r in range(rs,re+1))]
        if not cols: continue
        segs=[]; s=cols[0]; p=cols[0]
        for c in cols[1:]:
            if c>p+1:
                segs.append((s,p)); s=c
            p=c
        segs.append((s,p))
        widths=[ce-cs+1 for cs,ce in segs]
        cnt=Counter(widths)
        template_w=max((w for w in cnt if w>1), key=lambda x:(cnt[x],x), default=0)
        if template_w<=1: continue
        valid=[(cs,ce) for cs,ce in segs if ce-cs+1==template_w]
        if not valid: continue
        counts=[[Counter() for _ in range(template_w)] for _ in range(hb)]
        for cs,ce in valid:
            for dr in range(hb):
                for dc in range(template_w):
                    v=grid[rs+dr][cs+dc]
                    if v!=0:
                        counts[dr][dc][v]+=1
        template=[[0]*template_w for _ in range(hb)]
        for dr in range(hb):
            for dc in range(template_w):
                if counts[dr][dc]:
                    template[dr][dc]=max(counts[dr][dc], key=lambda x:(counts[dr][dc][x],x))
        for cs,ce in valid:
            for dr in range(hb):
                for dc in range(template_w):
                    out[rs+dr][cs+dc]=template[dr][dc]
    return out