import collections
def solve(grid):
    H, W = len(grid), len(grid[0])
    cnt = collections.Counter(c for row in grid for c in row)
    bg = max(cnt, key=cnt.get)
    vis = [[False]*W for _ in range(H)]
    zones = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] != bg and not vis[i][j]:
                q = collections.deque([(i,j)])
                vis[i][j] = True
                cells = []
                while q:
                    r,c = q.popleft()
                    cells.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<H and 0<=nc<W and not vis[nr][nc] and grid[nr][nc]!=bg:
                            vis[nr][nc] = True
                            q.append((nr,nc))
                r0 = min(r for r,c in cells)
                r1 = max(r for r,c in cells)
                c0 = min(c for r,c in cells)
                c1 = max(c for r,c in cells)
                h = r1-r0+1
                w = c1-c0+1
                pts = []
                for r,c in cells:
                    v = grid[r][c]
                    if v!=bg and v!=0:
                        pts.append((r-r0,c-c0,v))
                zones.append((r0,c0,h,w,pts))
    zones.sort(key=lambda z:(z[0],z[1]))
    out = [row[:] for row in grid]
    N = len(zones)
    for i in range(N):
        r0,c0,h,w,pts = zones[i]
        nr0,nc0,nh,nw,_ = zones[(i+1)%N]
        for lr,lc,v in pts:
            rr,cc = lc, h-1-lr
            if 0<=rr<nh and 0<=cc<nw:
                ar,ac = nr0+rr, nc0+cc
                if out[ar][ac]==0:
                    out[ar][ac] = v
    return out