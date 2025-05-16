from collections import deque
def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==5 and not visited[i][j]:
                q=deque([(i,j)])
                visited[i][j]=True
                pts=[(i,j)]
                while q:
                    r,c=q.popleft()
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc=r+dr,c+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and grid[nr][nc]==5:
                            visited[nr][nc]=True
                            q.append((nr,nc))
                            pts.append((nr,nc))
                clusters.append(pts)
    a,b = sorted(clusters, key=len)[:2]
    mask_frame = a
    shape_frame = b
    def bounds(pts):
        rs=[r for r,c in pts]; cs=[c for r,c in pts]
        return min(rs),max(rs),min(cs),max(cs)
    r1a,r2a,c1a,c2a = bounds(mask_frame)
    r1b,r2b,c1b,c2b = bounds(shape_frame)
    mi0, mj0 = r1a+1, c1a+1
    si0, sj0 = r1b+1, c1b+1
    mh, mw = r2a-r1a-1, c2a-c1a-1
    sh, sw = r2b-r1b-1, c2b-c1b-1
    mask = [(i,j) for i in range(mh) for j in range(mw) if grid[mi0+i][mj0+j]==0]
    vals = [grid[i][j] for i in range(si0, si0+sh) for j in range(sj0, sj0+sw) if grid[i][j] not in (0,5)]
    out = [row[:] for row in grid]
    for i in range(si0, si0+sh):
        for j in range(sj0, sj0+sw):
            if out[i][j] not in (0,):
                out[i][j]=0
    for k,(i,j) in enumerate(mask):
        if k<len(vals):
            out[si0+i][sj0+j] = vals[k]
    return out