def solve(grid):
    h=len(grid); w=len(grid[0])
    comp=[[-1]*w for _ in range(h)]
    comps=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0 and comp[i][j]<0:
                cid=len(comps)
                stack=[(i,j)]
                comp[i][j]=cid
                cells=[(i,j)]
                while stack:
                    x,y=stack.pop()
                    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and grid[nx][ny]!=0 and comp[nx][ny]<0:
                            comp[nx][ny]=cid
                            stack.append((nx,ny))
                            cells.append((nx,ny))
                has=False; c=0
                for x,y in cells:
                    if grid[x][y]>1:
                        has=True; c=grid[x][y]; break
                comps.append((cells,has,c))
    out=[row[:] for row in grid]
    for cells,has,c in comps:
        if not has: continue
        for x,y in cells:
            out[x][y]=c
        for x,y in cells:
            for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                nx,ny=x+dx,y+dy
                if 0<=nx<h and 0<=ny<w and grid[nx][ny]==1 and comp[nx][ny]!=comp[x][y]:
                    out[x][y]=c+1
                    break
    return out