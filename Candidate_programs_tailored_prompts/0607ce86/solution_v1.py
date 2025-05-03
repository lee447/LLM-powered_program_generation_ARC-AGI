def solve(grid):
    h=len(grid); w=len(grid[0])
    nz=[sum(1 for v in row if v>0) for row in grid]
    thr=max(nz)//2
    out=[]
    for i,row in enumerate(grid):
        if nz[i]<thr:
            out.append([0]*w)
        else:
            new=row[:]
            j=0
            while j<w:
                if row[j]>0:
                    k=j
                    while k<w and row[k]>0: k+=1
                    seg=row[j:k]
                    cnt={}
                    for v in seg: cnt[v]=cnt.get(v,0)+1
                    mv,maxc=max(cnt.items(),key=lambda x:x[1])
                    if maxc>(k-j)//2:
                        for x in range(j,k): new[x]=mv
                    j=k
                else:
                    j+=1
            out.append(new)
    return out