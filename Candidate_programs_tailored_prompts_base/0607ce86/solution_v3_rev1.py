from collections import Counter
def solve(grid):
    n,m=len(grid),len(grid[0])
    row_nz=[sum(1 for v in row if v!=0) for row in grid]
    thr=max(row_nz)//2
    band_rows=[i for i,c in enumerate(row_nz) if c>thr]
    segs=[]
    for i in band_rows:
        if not segs or i!=segs[-1][-1]+1:
            segs.append([i])
        else:
            segs[-1].append(i)
    lengths=[len(s) for s in segs]
    if not lengths:
        return [[0]*m for _ in range(n)]
    H=Counter(lengths).most_common(1)[0][0]
    blocks=[s for s in segs if len(s)==H]
    out=[[0]*m for _ in range(n)]
    canonical=[[0]*m for _ in range(H)]
    for k in range(H):
        for j in range(m):
            vals=[grid[s[0]+k][j] for s in blocks]
            c=Counter(vals)
            val, cnt=c.most_common(1)[0]
            ties=[v for v,cnt0 in c.items() if cnt0==cnt]
            canonical[k][j]=max(ties)
    for s in blocks:
        for k in range(H):
            out[s[0]+k]=canonical[k][:]
    return out