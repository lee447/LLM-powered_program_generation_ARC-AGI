def solve(grid):
    n=len(grid);m=len(grid[0])
    r1,r2=n,-1; c1,c2=m,-1
    for i in range(n):
        for j in range(m):
            if grid[i][j]==0:
                if i<r1: r1=i
                if i>r2: r2=i
                if j<c1: c1=j
                if j>c2: c2=j
    h=r2-r1+1; w=c2-c1+1
    mirror_intersect=False
    for c in range(c1,c2+1):
        mc=m-1-c
        if c1<=mc<=c2:
            mirror_intersect=True; break
    out=[]
    if mirror_intersect:
        for i in range(h):
            row=[]
            for j in range(w):
                row.append(grid[c1+j][r1+i])
            out.append(row)
    else:
        for i in range(h):
            row=[]
            for j in range(w):
                row.append(grid[r1+i][m-1-(c1+j)])
            out.append(row)
    return out