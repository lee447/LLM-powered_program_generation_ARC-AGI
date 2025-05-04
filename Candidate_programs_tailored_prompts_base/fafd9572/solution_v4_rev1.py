from collections import deque
def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    shapes = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not vis[i][j]:
                q=deque([(i,j)])
                vis[i][j]=True
                cells=[]
                while q:
                    x,y=q.popleft()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==1:
                            vis[nx][ny]=True
                            q.append((nx,ny))
                rs=[x for x,y in cells]; cs=[y for x,y in cells]
                r0,c0=min(rs),min(cs); r1,c1=max(rs),max(cs)
                ph, pw = r1-r0+1, c1-c0+1
                mask = [[0]*pw for _ in range(ph)]
                for x,y in cells:
                    mask[x-r0][y-c0]=1
                shapes.append((r0,c0,mask))
    shapes.sort(key=lambda t:(t[0],t[1]))
    anchors = [(r,c,grid[r][c]) for r in range(h) for c in range(w) if grid[r][c]!=0 and grid[r][c]!=1]
    anchors.sort(key=lambda t:(t[0],t[1]))
    g = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if g[i][j]==1:
                g[i][j]=0
    for i,(r0,c0,mask) in enumerate(shapes):
        if i<len(anchors):
            color=anchors[i][2]
            for dr in range(len(mask)):
                for dc in range(len(mask[0])):
                    if mask[dr][dc]:
                        g[r0+dr][c0+dc]=color
    return g