def solve(grid):
    from collections import deque
    R, C = len(grid), len(grid[0])
    vis = [[False]*C for _ in range(R)]
    clusters = []
    for i in range(R):
        for j in range(C):
            if grid[i][j]==3 and not vis[i][j]:
                q = deque([(i,j)])
                vis[i][j]=True
                pts = [(i,j)]
                while q:
                    r,c = q.popleft()
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc = r+dr, c+dc
                        if 0<=rr<R and 0<=cc<C and grid[rr][cc]==3 and not vis[rr][cc]:
                            vis[rr][cc]=True
                            q.append((rr,cc))
                            pts.append((rr,cc))
                rs = [r for r,_ in pts]; cs = [c for _,c in pts]
                min_r, max_r = min(rs), max(rs)
                min_c, max_c = min(cs), max(cs)
                clusters.append((min_r, min_c, max_r, max_c, pts))
    clusters.sort(key=lambda x:(x[0],x[1]))
    proc = [c for c in clusters if c[0]>0]
    out = [row[:] for row in grid]
    if proc:
        min_r, min_c, max_r, max_c, pts = proc[0]
        w = max_c-min_c+1
        dx = w+1
        for r,c in pts:
            if c+dx<C:
                out[r][c+dx] = 1
    if len(proc)>1:
        min_r, min_c, max_r, max_c, pts = proc[1]
        h = max_r-min_r+1
        dy = h+1
        if min_r-dy>=0:
            dr = -dy
        else:
            dr = dy
        for r,c in pts:
            if 0<=r+dr<R:
                out[r+dr][c] = 8
    return out