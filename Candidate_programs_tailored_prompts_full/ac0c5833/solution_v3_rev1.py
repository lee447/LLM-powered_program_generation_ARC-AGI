from collections import deque
def solve(grid):
    n, m = len(grid), len(grid[0])
    visited = [[False]*m for _ in range(n)]
    regions = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 4 and not visited[i][j]:
                q = deque([(i,j)])
                visited[i][j] = True
                pts = []
                mi, mj = i, j
                Ma_i, Ma_j = i, j
                while q:
                    x,y = q.popleft()
                    pts.append((x,y))
                    mi = min(mi, x); mj = min(mj, y)
                    Ma_i = max(Ma_i, x); Ma_j = max(Ma_j, y)
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0<=nx<n and 0<=ny<m and grid[nx][ny]!=4 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx,ny))
                h = Ma_i-mi+1; w = Ma_j-mj+1
                if len(pts)==h*w:
                    mask = [[0]*w for _ in range(h)]
                    has2 = False
                    for x,y in pts:
                        if grid[x][y]==2:
                            mask[x-mi][y-mj]=1
                            has2 = True
                    regions.append((mi,mj,h,w,has2,mask))
    pattern = None
    ph = pw = 0
    for mi,mj,h,w,has2,mask in regions:
        if has2:
            pattern = mask; ph, pw = h, w
            break
    out = [row[:] for row in grid]
    for mi,mj,h,w,has2,mask in regions:
        if not has2 and h==ph and w==pw:
            for di in range(h):
                for dj in range(w):
                    if pattern[di][dj]:
                        out[mi+di][mj+dj] = 2
    return out