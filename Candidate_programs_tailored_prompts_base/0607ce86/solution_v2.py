def solve(grid):
    H=len(grid); W=len(grid[0])
    is_blank=[all(c==0 for c in row) for row in grid]
    runs=[]
    r=0
    while r<H:
        if not is_blank[r]:
            start=r
            while r<H and not is_blank[r]:
                r+=1
            runs.append((start,r-start))
        else:
            r+=1
    from collections import Counter
    lengths=[l for _,l in runs]
    cnt=Counter(lengths)
    L=max(cnt, key=lambda x:cnt[x])
    runs_L=[s for s,l in runs if l==L]
    canon=[[0]*W for _ in range(L)]
    for i in range(L):
        for j in range(W):
            vals=[grid[s+i][j] for s in runs_L]
            vc=Counter(vals)
            canon[i][j]=max(vc, key=lambda x:(vc[x],x))
    res=[[0]*W for _ in range(H)]
    for s in runs_L:
        for i in range(L):
            res[s+i]=canon[i].copy()
    return res