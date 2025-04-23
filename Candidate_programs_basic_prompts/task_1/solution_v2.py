def solve(grid):
    h=len(grid); w=len(grid[0])
    nonzs=[sum(1 for v in row if v!=0) for row in grid]
    patternRows=[i for i,c in enumerate(nonzs) if c>4]
    if not patternRows:
        return [[0]*w for _ in range(h)]
    groupStarts=[patternRows[0]]+[
        patternRows[i] for i in range(1,len(patternRows))
        if patternRows[i]-patternRows[i-1]>1
    ]
    if len(groupStarts)>1:
        period=groupStarts[1]-groupStarts[0]
    else:
        period=len(patternRows)
    offsets=[i-groupStarts[0] for i in patternRows if i-groupStarts[0]<period]
    blocks=len(groupStarts)
    template={}
    for off in offsets:
        rowt=[]
        for j in range(w):
            cnt={}
            for k in range(blocks):
                r=groupStarts[k]+off
                if 0<=r<h:
                    v=grid[r][j]
                    cnt[v]=cnt.get(v,0)+1
            mv,mc=0,-1
            for v,c in cnt.items():
                if c>mc or (c==mc and v<mv):
                    mv,mc=v,c
            rowt.append(mv)
        template[off]=rowt
    out=[[0]*w for _ in range(h)]
    for k in range(blocks):
        base=groupStarts[k]
        for off in offsets:
            r=base+off
            if 0<=r<h:
                out[r]=template[off][:]
    return out