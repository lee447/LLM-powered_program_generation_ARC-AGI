def solve(grid):
    H=len(grid);W=len(grid[0])
    ys=[i for i in range(H) for j in range(W) if grid[i][j]==8]
    xs=[j for i in range(H) for j in range(W) if grid[i][j]==8]
    ymin,ymax=min(ys),max(ys);xmin,xmax=min(xs),max(xs)
    h=ymax-ymin+1;w=xmax-xmin+1
    top=None
    if ymin>0: top=grid[ymin-1][xmin:xmax+1]
    left=None
    if xmin>0:left=[grid[y][xmin-1] for y in range(ymin,ymax+1)]
    for r0 in range(H-h+1):
        for c0 in range(W-w+1):
            if r0<=ymin<=r0+h-1 and c0<=xmin<=c0+w-1:continue
            ok=True
            for i in range(h):
                for j in range(w):
                    if grid[r0+i][c0+j]==8:ok=False;break
                if not ok:break
            if not ok:continue
            if top is not None:
                if grid[r0-1][c0:c0+w]!=top:continue
            if left is not None:
                if [grid[r0+i][c0-1] for i in range(h)]!=left:continue
            return [grid[r0+i][c0:c0+w] for i in range(h)]
    return []