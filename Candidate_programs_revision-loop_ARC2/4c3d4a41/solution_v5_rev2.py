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
    small, large = sorted(clusters, key=len)
    def bounds(pts):
        rs=[r for r,c in pts]; cs=[c for r,c in pts]
        return min(rs),max(rs),min(cs),max(cs)
    r1s,r2s,c1s,c2s = bounds(small)
    r1l,r2l,c1l,c2l = bounds(large)
    si0, sj0 = r1s+1, c1s+1
    sh, sw = r2s-r1s-1, c2s-c1s-1
    mi0, mj0 = r1l+1, c1l+1
    mh, mw = r2l-r1l-1, c2l-c1l-1
    vals = [grid[i][j] for i in range(mi0, mi0+mh) for j in range(mj0, mj0+mw) if grid[i][j] not in (0,5)]
    out = [row[:] for row in grid]
    for i in range(si0, si0+sh):
        for j in range(sj0, sj0+sw):
            out[i][j]=0
    for k,(i,j) in enumerate([(i,j) for i in range(mh) for j in range(mw) if grid[mi0+i][mj0+j] not in (0,5)]):
        if k<len(vals):
            out[si0+i][sj0+j]=vals[k]
    return out