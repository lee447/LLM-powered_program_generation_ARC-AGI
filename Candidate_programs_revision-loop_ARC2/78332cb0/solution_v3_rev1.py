def solve(grid):
    n=len(grid);m=len(grid[0])
    seprows=[i for i in range(n) if all(grid[i][j]==6 for j in range(m))]
    sepcols=[j for j in range(m) if all(grid[i][j]==6 for i in range(n))]
    rs=[];prev=0
    for i in sorted(seprows):
        if prev<i:rs.append((prev,i))
        prev=i+1
    if prev<n:rs.append((prev,n))
    cs=[];prev=0
    for j in sorted(sepcols):
        if prev<j:cs.append((prev,j))
        prev=j+1
    if prev<m:cs.append((prev,m))
    R=len(rs);C=len(cs)
    blocks=[[ [row[c0:c1] for row in grid[r0:r1]] for c0,c1 in cs] for r0,r1 in rs]
    if R*C==1:
        return grid
    if (R>1 and C==1) or (R==1 and C>1):
        if R>1 and C==1:
            seq=[blocks[i][0] for i in range(R-1,-1,-1)]
        else:
            seq=[blocks[0][j] for j in range(C)]
        h=len(seq[0])
        out=[]
        for i in range(h):
            row=[]
            for k,b in enumerate(seq):
                row+=b[i]
                if k!=len(seq)-1:row.append(6)
            out.append(row)
        return out
    seq=[]
    for j in range(C):
        for i in range(R):
            seq.append(blocks[i][j])
    h=len(seq[0]);w=len(seq[0][0])
    out=[]
    for k,b in enumerate(seq):
        for row in b:
            out.append(row[:])
        if k!=len(seq)-1:
            out.append([6]*w)
    return out