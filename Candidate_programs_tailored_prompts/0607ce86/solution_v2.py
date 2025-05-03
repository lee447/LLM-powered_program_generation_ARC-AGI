def solve(grid):
    h=len(grid); w=len(grid[0])
    zero_row=[0]*w
    bands=[]
    in_band=False
    for r in range(h):
        if not in_band and any(grid[r][c]!=0 for c in range(w)):
            start=r; in_band=True
        if in_band and all(grid[r][c]==0 for c in range(w)):
            bands.append((start,r-1)); in_band=False
    if in_band: bands.append((start,h-1))
    out=[zero_row[:] for _ in range(h)]
    for start,end in bands:
        rows=list(range(start,end+1))
        bh=len(rows)
        cnt=[0]*w
        for c in range(w):
            for r in rows:
                if grid[r][c]!=0: cnt[c]+=1
        mask=[cnt[c]>bh/2 for c in range(w)]
        motif_rows=[r for r in rows if all(grid[r][c]!=0 for c in range(w) if mask[c])]
        groups={}
        for r in motif_rows:
            key=tuple(grid[r][c] for c in range(w) if mask[c])
            groups.setdefault(key,[]).append(r)
        for key,rs in groups.items():
            canon=[0]*w
            for ci,c in enumerate([c for c in range(w) if mask[c]]):
                freq={}
                for r in rs:
                    v=grid[r][c]; freq[v]=freq.get(v,0)+1
                canon[c]=max(freq.items(),key=lambda x:(x[1],x[0]))[0]
            for r in rs:
                out[r]=canon[:]
    return out