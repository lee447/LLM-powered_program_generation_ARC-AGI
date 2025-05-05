from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    g = [row[:] for row in grid]
    seen = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==5 and not seen[i][j]:
                stack=[(i,j)]
                seen[i][j]=True
                cells=[]
                while stack:
                    x,y=stack.pop()
                    cells.append((x,y))
                    for dx,dy in dirs:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==5:
                            seen[nx][ny]=True
                            stack.append((nx,ny))
                xs=[x for x,y in cells]
                ys=[y for x,y in cells]
                clusters.append((min(xs),max(xs),min(ys),max(ys)))
    for minx,maxx,miny,maxy in clusters:
        for x in range(minx+1, maxx):
            for y in range(miny+1, maxy):
                if g[x][y]==0:
                    g[x][y]=2
        top = sum(grid[minx][y]==5 for y in range(miny, maxy+1))
        bot = sum(grid[maxx][y]==5 for y in range(miny, maxy+1))
        left = sum(grid[x][miny]==5 for x in range(minx, maxx+1))
        right = sum(grid[x][maxy]==5 for x in range(minx, maxx+1))
        side = min((top,"top"),(bot,"bot"),(left,"left"),(right,"right"))[1]
        if side=="top":
            r = minx-1
            if 0<=r<h:
                for y in range(miny, maxy+1):
                    if g[r][y]==0:
                        g[r][y]=2
        elif side=="bot":
            r = maxx+1
            if 0<=r<h:
                for y in range(miny, maxy+1):
                    if g[r][y]==0:
                        g[r][y]=2
        elif side=="left":
            c = miny-1
            if 0<=c<w:
                for x in range(minx, maxx+1):
                    if g[x][c]==0:
                        g[x][c]=2
        else:
            c = maxy+1
            if 0<=c<w:
                for x in range(minx, maxx+1):
                    if g[x][c]==0:
                        g[x][c]=2
    return g