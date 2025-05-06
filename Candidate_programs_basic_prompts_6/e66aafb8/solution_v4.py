def solve(grid):
    H=len(grid);W=len(grid[0])
    y0=0
    while y0<H and 0 not in grid[y0]:
        y0+=1
    row0=grid[y0]
    x0=row0.index(0)
    x1=W-1-row0[::-1].index(0)
    y1=y0
    while y1<H and all(grid[y1][x]==0 for x in range(x0,x1+1)):
        y1+=1
    h=y1-y0; w=x1-x0+1
    out=[]
    for i in range(h):
        y=H-1-(y0+i)
        out.append([grid[y][x0+j] for j in range(w)])
    return out