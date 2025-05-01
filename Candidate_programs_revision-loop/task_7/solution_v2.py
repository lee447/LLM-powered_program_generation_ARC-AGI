def solve(grid):
    H=len(grid);W=len(grid[0])
    rows=[-1]+[r for r in range(H) if all(grid[r][c]==4 for c in range(W))]+[H]
    cols=[-1]+[c for c in range(W) if all(grid[r][c]==4 for r in range(H))]+[W]
    rooms=[]
    for i in range(len(rows)-1):
        r0,r1=rows[i],rows[i+1]
        if r1-r0<2:continue
        for j in range(len(cols)-1):
            c0,c1=cols[j],cols[j+1]
            if c1-c0<2:continue
            rooms.append((r0+1,r1-1,c0+1,c1-1))
    master=None
    for r0,r1,c0,c1 in rooms:
        s={grid[r][c] for r in range(r0,r1+1) for c in range(c0,c1+1)}
        vs=s-{0}
        if len(vs)==1 and next(iter(vs))!=1 and 1 not in s:
            master=(r0,r1,c0,c1,next(iter(vs)))
            break
    if not master: return grid
    r0,r1,c0,c1,col=master
    mask=[[grid[r][c]==col for c in range(c0,c1+1)] for r in range(r0,r1+1)]
    out=[row[:] for row in grid]
    for rr0,rr1,cc0,cc1 in rooms:
        if (rr0,rr1,cc0,cc1)==(r0,r1,c0,c1):continue
        s={grid[r][c] for r in range(rr0,rr1+1) for c in range(cc0,cc1+1)}
        if s-{0,1}==set() and 1 in s:
            for i in range(rr1-rr0+1):
                for j in range(cc1-cc0+1):
                    if mask[i][j] and out[rr0+i][cc0+j]==1:
                        out[rr0+i][cc0+j]=col
    return out