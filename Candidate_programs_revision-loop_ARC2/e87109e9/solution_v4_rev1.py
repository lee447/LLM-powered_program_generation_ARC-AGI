from collections import Counter
def solve(grid):
    n,m=len(grid),len(grid[0])
    ur={i for i in range(n) if len(set(grid[i]))==1}
    uc={j for j in range(m) if len({grid[i][j] for i in range(n)})==1}
    rows=[i for i in range(n) if i not in ur]
    cols=[j for j in range(m) if j not in uc]
    sub=[[grid[i][j] for j in cols] for i in rows]
    cnt=Counter(v for row in sub for v in row)
    motif=min((c for c in cnt if cnt[c]>1),key=cnt.__getitem__)
    R,C=len(sub),len(sub[0])
    minr=min(i for i in range(R) for j in range(C) if sub[i][j]==motif)
    maxr=max(i for i in range(R) for j in range(C) if sub[i][j]==motif)
    minc=min(j for i in range(R) for j in range(C) if sub[i][j]==motif)
    maxc=max(j for i in range(R) for j in range(C) if sub[i][j]==motif)
    h,w=maxr-minr+1,maxc-minc+1
    offs=[(i-minr,j-minc) for i in range(minr,minr+h) for j in range(minc,minc+w) if sub[i][j]==motif]
    # original row intervals
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
    rh=[r2-r1+1 for r1,r2 in ris]
    cw=[c2-c1+1 for c1,c2 in cis]
    sr=[0]
    for x in rh: sr.append(sr[-1]+x)
    sc=[0]
    for x in cw: sc.append(sc[-1]+x)
    for bi in range(len(rh)):
        for bj in range(len(cw)):
            r0=sr[bi]
            c0=sc[bj]
            rhh=rh[bi]; cww=cw[bj]
            si=r0+(rhh-h)//2
            sj=c0+(cww-w)//2
            for dr,dc in offs:
                sub[si+dr][sj+dc]=motif
    return sub