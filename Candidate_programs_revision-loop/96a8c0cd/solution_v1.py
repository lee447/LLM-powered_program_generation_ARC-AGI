def solve(grid):
    H=len(grid); W=len(grid[0])
    M=[row[:] for row in grid]
    visited=[[False]*W for _ in range(H)]
    shapes=[]
    for i in range(H):
        for j in range(W):
            if grid[i][j]!=0 and grid[i][j]!=2 and not visited[i][j]:
                c=grid[i][j]
                stack=[(i,j)]
                visited[i][j]=True
                cells=[(i,j)]
                while stack:
                    x,y=stack.pop()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and not visited[nx][ny] and grid[nx][ny]==c:
                            visited[nx][ny]=True
                            stack.append((nx,ny))
                            cells.append((nx,ny))
                rs=[r for r,_ in cells]; cs=[c0 for _,c0 in cells]
                shapes.append((c, min(rs), max(rs), min(cs), max(cs)))
    from collections import defaultdict
    vert=defaultdict(list)
    horz=defaultdict(list)
    for c,r0,r1,c0,c1 in shapes:
        if r1>r0:
            vert[(r0,r1,c)].append((r0,r1,c0,c1))
        elif c1>c0:
            horz[(c0,c1,c)].append((r0,r1,c0,c1))
    for (r0,r1,c),g in vert.items():
        if len(g)>1:
            rmid=(r0+r1)//2
            g.sort(key=lambda x: x[2])
            for (_,_,c0a,_),( _,_,c0b,_) in zip(g, g[1:]):
                for y in range(c0a+1, c0b):
                    if M[rmid][y]==0: M[rmid][y]=2
    for (c0,c1,c),g in horz.items():
        if len(g)>1:
            cmid=(c0+c1)//2
            g.sort(key=lambda x: x[0])
            for (r0a,_,_,_),(r0b,_,_,_) in zip(g, g[1:]):
                for x in range(r0a+1, r0b):
                    if M[x][cmid]==0: M[x][cmid]=2
    return M