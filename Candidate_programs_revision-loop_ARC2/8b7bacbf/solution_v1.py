def solve(grid):
    H=len(grid);W=len(grid[0])
    freq={}
    for r in grid:
        for v in r:
            freq[v]=freq.get(v,0)+1
    fill_color=next(k for k,v in freq.items() if k!=0 and v==1)
    out=[row[:] for row in grid]
    vis=[[False]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if grid[i][j]==0 and not vis[i][j]:
                stack=[(i,j)]
                vis[i][j]=True
                comp=[]
                border=False
                while stack:
                    x,y=stack.pop()
                    comp.append((x,y))
                    if x==0 or y==0 or x==H-1 or y==W-1:
                        border=True
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and not vis[nx][ny] and grid[nx][ny]==0:
                            vis[nx][ny]=True
                            stack.append((nx,ny))
                if border:continue
                bset=set()
                for x,y in comp:
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and grid[nx][ny]!=0:
                            bset.add(grid[nx][ny])
                if len(bset)==1 and next(iter(bset))!=fill_color:
                    for x,y in comp:
                        out[x][y]=fill_color
    return out