def solve(grid):
    H=len(grid);W=len(grid[0])
    res=[row[:] for row in grid]
    visited=set()
    for i in range(H):
        for j in range(W):
            if grid[i][j]==8 and (i,j) not in visited:
                cluster=[]
                stack=[(i,j)]
                visited.add((i,j))
                while stack:
                    x,y=stack.pop()
                    cluster.append((x,y))
                    for dx in(-1,0,1):
                        for dy in(-1,0,1):
                            if dx==0 and dy==0: continue
                            nx,ny=x+dx,y+dy
                            if 0<=nx<H and 0<=ny<W and grid[nx][ny]==8 and (nx,ny) not in visited:
                                visited.add((nx,ny))
                                stack.append((nx,ny))
                mi=min(x for x,y in cluster); ma=max(x for x,y in cluster)
                mj=min(y for x,y in cluster); mj2=max(y for x,y in cluster)
                for x in range(mi,ma+1):
                    for y in range(mj,mj2+1):
                        if res[x][y]==0: res[x][y]=2
    return res