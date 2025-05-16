from collections import deque
def solve(grid):
    h,w=len(grid),len(grid[0])
    regs=sorted({v for row in grid for v in row if v!=0})
    visited=[[False]*w for _ in range(h)]
    out=[row[:] for row in grid]
    flips=[]
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==0 and not visited[i][j]:
                q=deque([(i,j)])
                visited[i][j]=True
                comp=[]
                neighbor_colors=set()
                while q:
                    x,y=q.popleft()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w:
                            if grid[nx][ny]==0 and not visited[nx][ny]:
                                visited[nx][ny]=True
                                q.append((nx,ny))
                            elif grid[nx][ny]!=0:
                                neighbor_colors.add(grid[nx][ny])
                if len(neighbor_colors)==1:
                    c=next(iter(neighbor_colors))
                    other=regs[1] if regs[0]==c else regs[0]
                    for x,y in comp:
                        out[x][y]=8
                    for x,y in comp:
                        for dx,dy in dirs:
                            nx,ny=x+dx,y+dy
                            if 0<=nx<h and 0<=ny<w and grid[nx][ny]==c:
                                flips.append((nx,ny,other))
    for x,y,oc in flips:
        out[x][y]=oc
    return out