from collections import Counter
def solve(grid):
    n,m=len(grid),len(grid[0])
    ur={i for i in range(n) if len(set(grid[i]))==1}
    uc={j for j in range(m) if len({grid[i][j] for i in range(n)})==1}
    ris=[]
    i=0
    while i<n:
        if i not in ur:
            a=i
            while i<n and i not in ur: i+=1
            ris.append((a,i-1))
        else:
            i+=1
    cis=[]
    j=0
    while j<m:
        if j not in uc:
            a=j
            while j<m and j not in uc: j+=1
            cis.append((a,j-1))
        else:
            j+=1
    cnt=Counter()
    for r1,r2 in ris:
        for c1,c2 in cis:
            for i in range(r1,r2+1):
                for j in range(c1,c2+1):
                    cnt[grid[i][j]]+=1
    motif=min([c for c,v in cnt.items() if v>1], key=lambda c:cnt[c])
    br=bj=None
    for bi,(r1,r2) in enumerate(ris):
        for bj,(c1,c2) in enumerate(cis):
            if any(grid[i][j]==motif for i in range(r1,r2+1) for j in range(c1,c2+1)):
                br,bc=bi,bj
                break
        if br is not None: break
    r1,r2=ris[br]
    c1,c2=cis[bc]
    minr=min(i for i in range(r1,r2+1) for j in range(c1,c2+1) if grid[i][j]==motif)
    maxr=max(i for i in range(r1,r2+1) for j in range(c1,c2+1) if grid[i][j]==motif)
    minc=min(j for i in range(r1,r2+1) for j in range(c1,c2+1) if grid[i][j]==motif)
    maxc=max(j for i in range(r1,r2+1) for j in range(c1,c2+1) if grid[i][j]==motif)
    h,w=maxr-minr+1,maxc-minc+1
    offs=[(i-minr,j-minc) for i in range(minr,maxr+1) for j in range(minc,maxc+1) if grid[i][j]==motif]
    for r1,r2 in ris:
        H=r2-r1+1
        for c1,c2 in cis:
            W=c2-c1+1
            top=r1+(H-h)//2
            left=c1+(W-w)//2
            for dr,dc in offs:
                grid[top+dr][left+dc]=motif
    return grid