def solve(grid):
    R=len(grid);C=len(grid[0])
    hs=[i for i in range(R) if len(set(grid[i]))==1]
    vs=[j for j in range(C) if len({grid[i][j] for i in range(R)})==1]
    rb=[-1]+hs+[R];cb=[-1]+vs+[C]
    rows=[] 
    for k in range(len(rb)-1):
        s=rb[k]+1; e=rb[k+1]-1
        if s<=e: rows.append((s,e))
    cols=[] 
    for k in range(len(cb)-1):
        s=cb[k]+1; e=cb[k+1]-1
        if s<=e: cols.append((s,e))
    out=[[0]*len(cols) for _ in rows]
    for i,(r0,_) in enumerate(rows):
        for j,(c0,_) in enumerate(cols):
            out[i][j]=grid[r0][c0]
    return out