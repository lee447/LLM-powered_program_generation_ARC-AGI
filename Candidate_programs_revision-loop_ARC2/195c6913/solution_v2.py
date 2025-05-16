def solve(grid):
    h=len(grid);w=len(grid[0])
    from collections import Counter,deque
    cnt=Counter(c for row in grid for c in row)
    bc=cnt.most_common()[-1][0]
    mc=[c for c,_ in cnt.most_common(3) if c!=bc]
    frame=set(mc[:2])
    objs=[]
    seen=[[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            c=grid[i][j]
            if c not in frame and c!=bc and not seen[i][j]:
                q=deque([(i,j)]);seen[i][j]=True;comp=[]
                while q:
                    x,y=q.popleft();comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==c:
                            seen[nx][ny]=True;q.append((nx,ny))
                objs.append(comp)
    objs.sort(key=lambda comp:(min(r+c for r,c in comp),grid[comp[0][0]][comp[0][1]]))
    path=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j] in frame:
                for dx,dy in ((1,0),(0,1)):
                    ni,nj=i+dx,j+dy
                    if 0<=ni<h and 0<=nj<w and grid[ni][nj] in frame and grid[i][j]!=grid[ni][nj]:
                        path.append((i,j))
                        break
    path=sorted(set(path),key=lambda x:(x[0]+x[1],x[0],x[1]))
    out=[row[:] for row in grid]
    for idx,comp in enumerate(objs):
        if idx>=len(path):break
        r,c=path[idx]
        pts=sorted(comp,key=lambda x:(x[0],x[1]))
        for k,(x,y) in enumerate(pts):
            if c+k<w: out[r][c+k]=grid[x][y]
    return out