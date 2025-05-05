import collections
def solve(grid):
    h, w = len(grid), len(grid[0])
    target = next((v for row in grid for v in row if v!=0),0)
    visited = [[False]*w for _ in range(h)]
    comps = []
    for y in range(h):
        for x in range(w):
            if not visited[y][x] and grid[y][x]==target:
                pts = []
                q = [(y,x)]
                visited[y][x]=True
                while q:
                    yy,xx = q.pop()
                    pts.append((yy,xx))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx = yy+dy,xx+dx
                        if 0<=ny<h and 0<=nx<w and not visited[ny][nx] and grid[ny][nx]==target:
                            visited[ny][nx]=True
                            q.append((ny,nx))
                ys = [p[0] for p in pts]; xs = [p[1] for p in pts]
                comps.append((min(ys),max(ys),min(xs),max(xs),pts))
    if len(comps)!=3:
        return grid
    comps_y = sorted(comps, key=lambda c:c[0])
    mid = comps_y[1]
    mid_y0,mid_y1,mid_x0,mid_x1,_ = mid
    row = mid_y0+1
    res = [row[:] for row in grid]
    for c in comps_y:
        if c is mid: continue
        y0,y1,x0,x1,_ = c
        if x1<mid_x0:
            for cc in range(x1+1, mid_x0):
                if 0<=row<h and 0<=cc<w and res[row][cc]==0:
                    res[row][cc]=target
        elif x0>mid_x1:
            for cc in range(mid_x1+1, x0):
                if 0<=row<h and 0<=cc<w and res[row][cc]==0:
                    res[row][cc]=target
    return res