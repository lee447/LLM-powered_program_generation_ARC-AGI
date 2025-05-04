def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import deque
    g = [row[:] for row in grid]
    seen = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not seen[i][j]:
                # BFS for component
                q = deque([(i,j)])
                comp = [(i,j)]
                seen[i][j] = True
                while q:
                    x,y = q.popleft()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==1:
                            seen[nx][ny]=True
                            q.append((nx,ny))
                            comp.append((nx,ny))
                minx = min(x for x,y in comp)
                maxx = max(x for x,y in comp)
                miny = min(y for x,y in comp)
                maxy = max(y for x,y in comp)
                H = maxx-minx+1
                W = maxy-miny+1
                # line rules
                if H==1 and W>2:
                    do = True
                elif W==1 and H>1:
                    do = True
                else:
                    # check full opposite sides
                    top = all(grid[minx][y]==1 for y in range(miny,maxy+1))
                    bot = all(grid[maxx][y]==1 for y in range(miny,maxy+1))
                    left = all(grid[x][miny]==1 for x in range(minx,maxx+1))
                    right = all(grid[x][maxy]==1 for x in range(minx,maxx+1))
                    do = (left and right) or (top and bot)
                if do:
                    for x,y in comp:
                        g[x][y] = 2
    return g