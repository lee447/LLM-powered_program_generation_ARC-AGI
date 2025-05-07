def solve(grid):
    H=len(grid);W=len(grid[0])
    bounds={}
    for r in range(H):
        for c in range(W):
            v=grid[r][c]
            if v:
                if v not in bounds:
                    bounds[v]=[r,c,r,c]
                else:
                    b=bounds[v]
                    if r<b[0]:b[0]=r
                    if c<b[1]:b[1]=c
                    if r>b[2]:b[2]=r
                    if c>b[3]:b[3]=c
    shapes=sorted([(b[0],b[1],b[2],b[3],col) for col,b in bounds.items()],key=lambda x:(x[0],x[1]))
    res=[row[:] for row in grid]
    for minr,minc,maxr,maxc,col in reversed(shapes):
        for r in range(minr,maxr+1):
            for c in range(minc,maxc+1):
                res[r][c]=col
    return res