from collections import Counter
def solve(grid):
    h=len(grid); w=len(grid[0])
    nz=[sum(1 for v in row if v!=0) for row in grid]
    thr=max(nz)//2
    kept=[i for i,c in enumerate(nz) if c>=thr]
    starts=[]
    for i in kept:
        row=grid[i]; j=0
        while j<w:
            if row[j]!=0:
                starts.append(j)
                k=j+1
                while k<w and row[k]!=0: k+=1
                j=k
            else:
                j+=1
    sc=Counter(starts)
    t2=max(1,len(kept)//2)
    bs=sorted(s for s,c in sc.items() if c>=t2)
    widths=[]
    for i in kept:
        for s in bs:
            if s<w and grid[i][s]!=0:
                k=s
                while k<w and grid[i][k]!=0: k+=1
                widths.append(k-s)
    bw=Counter(widths).most_common(1)[0][0] if widths else 0
    out=[[0]*w for _ in range(h)]
    for i in range(h):
        if nz[i]<thr: continue
        tpl=[0]*bw
        for k in range(bw):
            vals=[grid[i][s+k] for s in bs if s+k<w and grid[i][s+k]!=0]
            tpl[k]=Counter(vals).most_common(1)[0][0] if vals else 0
        for s in bs:
            for k in range(bw):
                if s+k<w: out[i][s+k]=tpl[k]
    return out