def solve(grid):
    h,w=len(grid),len(grid[0])
    g=[row[:]for row in grid]
    visited=[[False]*w for _ in range(h)]
    dirs=[(-1,-1),(-1,1),(1,-1),(1,1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==6 and not visited[i][j]:
                stack=[(i,j)]
                visited[i][j]=True
                region=[]
                while stack:
                    x,y=stack.pop()
                    region.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==6:
                            visited[nx][ny]=True
                            stack.append((nx,ny))
                stats=[]
                for dr,dc in dirs:
                    fail=0
                    seen=set()
                    for x,y in region:
                        k=1
                        while True:
                            nx,ny=x+dr*k,y+dc*k
                            if not (0<=nx<h and 0<=ny<w):
                                fail+=1
                                break
                            if grid[nx][ny]!=6:
                                seen.add(grid[nx][ny])
                                break
                            k+=1
                    stats.append((dr,dc,fail,seen))
                best_fail=min(s[2] for s in stats)
                cands=[s for s in stats if s[2]==best_fail]
                dr,dc=max(cands,key=lambda x:len(x[3]))[:2]
                for x,y in region:
                    k=1
                    while True:
                        nx,ny=x+dr*k,y+dc*k
                        if not (0<=nx<h and 0<=ny<w): break
                        if grid[nx][ny]!=6:
                            g[x][y]=grid[nx][ny]
                            break
                        k+=1
    return g