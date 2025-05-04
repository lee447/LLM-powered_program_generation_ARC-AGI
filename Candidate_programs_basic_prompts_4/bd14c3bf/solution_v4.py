def solve(grid):
    h, w = len(grid), len(grid[0])
    g = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    from collections import deque
    template_color = None
    for i in range(h):
        for j in range(w):
            if g[i][j] > 1 and not visited[i][j]:
                c = g[i][j]
                q = deque([(i,j)])
                visited[i][j] = True
                cells = [(i,j)]
                while q:
                    x,y = q.popleft()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and g[nx][ny]==c:
                            visited[nx][ny] = True
                            q.append((nx,ny))
                            cells.append((nx,ny))
                mi = min(x for x,y in cells); ma = max(x for x,y in cells)
                mj = min(y for x,y in cells); mb = max(y for x,y in cells)
                area = (ma-mi+1)*(mb-mj+1)
                if len(cells)==area and len(cells)>1:
                    template_color = c
                    break
        if template_color is not None:
            break
    visited = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if g[i][j]==1 and not visited[i][j]:
                q = deque([(i,j)])
                visited[i][j] = True
                cells = [(i,j)]
                while q:
                    x,y = q.popleft()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and g[nx][ny]==1:
                            visited[nx][ny] = True
                            q.append((nx,ny))
                            cells.append((nx,ny))
                mi = min(x for x,y in cells); ma = max(x for x,y in cells)
                mj = min(y for x,y in cells); mb = max(y for x,y in cells)
                H, W = ma-mi+1, mb-mj+1
                sz = len(cells)
                if sz>=3 and ((H==1) or (W==1) or (H>=3 and W>=3)):
                    ok = True
                    for x,y in cells:
                        if not (x==mi or x==ma or y==mj or y==mb):
                            ok = False
                            break
                    if ok and template_color is not None:
                        for x,y in cells:
                            g[x][y] = template_color
    return g