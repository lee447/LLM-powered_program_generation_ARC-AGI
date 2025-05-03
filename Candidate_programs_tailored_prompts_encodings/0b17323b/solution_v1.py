def solve(grid):
    h=len(grid);w=len(grid[0])
    n=min(h,w)
    rlist=[i for i in range(n) if grid[i][i]==1]
    rset=set(rlist)
    seqs=[]
    for a in rlist:
        for b in rlist:
            if b>a:
                step=b-a
                if (a-step) not in rset:
                    seq=[a]
                    x=a+step
                    while x in rset:
                        seq.append(x);x+=step
                    if len(seq)>=3:
                        seqs.append((step,seq))
    res=[row.copy() for row in grid]
    for step,seq in seqs:
        x=seq[-1]+step
        while x<n:
            if res[x][x]==0:res[x][x]=2
            x+=step
    return res