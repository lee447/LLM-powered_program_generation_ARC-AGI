from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H,W=len(grid),len(grid[0])
    h2,w2=H//2,W//2
    quads={
        'TL':[row[:w2] for row in grid[:h2]],
        'TR':[row[w2:] for row in grid[:h2]],
        'BL':[row[:w2] for row in grid[h2:]],
        'BR':[row[w2:] for row in grid[h2:]]
    }
    def uniq(a):
        s=set()
        for r in a:
            s|=set(r)
        return s
    def nonzero(a):
        return {x for x in uniq(a) if x!=0}
    # identify fill quad: two nonzero colors, no holes
    fill_name=next(name for name,m in quads.items() if 0 not in uniq(m) and len(nonzero(m))==2)
    fill=quads[fill_name]
    # identify mask quad: has holes and exactly one nonzero color
    mask_name=next(name for name,m in quads.items() if 0 in uniq(m) and len(nonzero(m))==1)
    mask=quads[mask_name]
    # extract mask tile by finding minimal period
    def period(a):
        h,w=len(a),len(a[0])
        for ph in range(1,h+1):
            if h%ph==0 and all(a[i]==a[i%ph] for i in range(h)):
                th=ph; break
        for pw in range(1,w+1):
            if w%pw==0 and all(a[i][j]==a[i][j%pw] for i in range(h) for j in range(w)):
                tw=pw; break
        return th,tw
    th,tw=period(mask)
    tile=[row[:tw] for row in mask[:th]]
    # fill holes
    fcol=next(iter(nonzero(fill)))
    tile=[[fcol if v==0 else v for v in row] for row in tile]
    # tile out
    fu=nonzero(fill)
    if len(fu)>1:
        rc,cc=len(fill),len(fill[0])
    else:
        rc,cc=len(fill),1
    out=[]
    for i in range(rc*th):
        r=[]
        for j in range(cc*tw):
            r.append(tile[i%th][j%tw])
        out.append(r)
    return out