from collections import deque
def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    expand = {2:2, 4:2, 3:3, 6:3}
    visited = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and (grid[i][j]==1 or grid[i][j] in expand):
                q = deque([(i,j)])
                comp = []
                seeds = []
                visited[i][j] = True
                while q:
                    x,y = q.popleft()
                    comp.append((x,y))
                    if grid[x][y] in expand:
                        seeds.append((x,y,grid[x][y]))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and (grid[nx][ny]==1 or grid[nx][ny] in expand):
                            visited[nx][ny] = True
                            q.append((nx,ny))
                if seeds:
                    _,__,c = seeds[0]
                    s = expand[c]
                    is_ = [x for x,_ in comp]
                    js_ = [y for _,y in comp]
                    mi,ma = min(is_), max(is_)
                    mj,na = min(js_), max(js_)
                    H_int = ma - mi - 1
                    W_int = na - mj - 1
                    if H_int>0 and W_int>0:
                        rfill = min(s, H_int)
                        cfill = min(s, W_int)
                        ro = (H_int - rfill)//2
                        co = (W_int - cfill)//2
                        rs = mi + 1 + ro
                        cs = mj + 1 + co
                        for di in range(rfill):
                            for dj in range(cfill):
                                res[rs+di][cs+dj] = c
    return res