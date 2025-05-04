def solve(grid):
    h=len(grid);w=len(grid[0])
    seen=[[False]*w for _ in range(h)]
    comps=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==0 and not seen[i][j]:
                stack=[(i,j)];seen[i][j]=True;cells=[]
                while stack:
                    x,y=stack.pop()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==0:
                            seen[nx][ny]=True
                            stack.append((nx,ny))
                comps.append(cells)
    best=None;best_c=None
    for cells in comps:
        cx=sum(c for _,c in cells)/len(cells)
        if best_c is None or cx<best_c:
            best_c=cx;best=cells
    out=[row[:] for row in grid]
    for x,y in best:
        out[x][y]=3
    return out