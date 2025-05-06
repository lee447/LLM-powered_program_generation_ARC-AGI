def solve(grid):
    from collections import Counter
    n=len(grid); m=len(grid[0])
    row_counts=[sum(1 for v in row if v!=0) for row in grid]
    mc=max(row_counts)
    if mc==0: return [[0]*m for _ in range(n)]
    thr_row=mc/2
    nzr=[i for i,c in enumerate(row_counts) if c>thr_row]
    bands=[]
    for r in nzr:
        if not bands or r!=bands[-1][-1]+1:
            bands.append([r])
        else:
            bands[-1].append(r)
    first_band=bands[0]
    h=len(first_band)
    col_counts=[sum(1 for r in first_band if grid[r][c]!=0) for c in range(m)]
    thr_col=h/2
    cand_cols=[c for c,cc in enumerate(col_counts) if cc>thr_col]
    segs=[]
    if cand_cols:
        s=cand_cols[0]; p=s
        for c in cand_cols[1:]:
            if c==p+1:
                p=c
            else:
                segs.append((s,p-s+1)); s=c; p=c
        segs.append((s,p-s+1))
    blocks=[]
    for x,w in segs:
        b=[[grid[r][c] for c in range(x,x+w)] for r in first_band]
        blocks.append(b)
    prot=[[0]*segs[0][1] for _ in range(h)]
    for i in range(h):
        for j in range(segs[0][1]):
            vals=[b[i][j] for b in blocks]
            prot[i][j]=Counter(vals).most_common(1)[0][0]
    out=[[0]*m for _ in range(n)]
    for band in bands:
        r0=band[0]
        for x,w in segs:
            for i in range(h):
                for j in range(w):
                    out[r0+i][x+j]=prot[i][j]
    return out