def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if not vis[i][j] and grid[i][j] in (2,5):
                pts = [(i,j)]
                vis[i][j] = True
                q = [(i,j)]
                for r,c in q:
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc = r+dr, c+dc
                        if 0<=rr<h and 0<=cc<w and not vis[rr][cc] and grid[rr][cc] in (2,5):
                            vis[rr][cc] = True
                            q.append((rr,cc))
                            pts.append((rr,cc))
                clusters.append(pts)
    opens = []
    for pts in clusters:
        s = set(pts)
        for r,c in pts:
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                rr,cc = r+dr, c+dc
                if 0<=rr<h and 0<=cc<w and grid[rr][cc]==0:
                    cnt = 0
                    for dr2,dc2 in ((1,0),(-1,0),(0,1),(0,-1)):
                        r2,c2 = rr+dr2, cc+dc2
                        if 0<=r2<h and 0<=c2<w and grid[r2][c2]==2:
                            cnt += 1
                    if cnt>=2:
                        opens.append((rr,cc))
                        break
            if len(opens)==len(clusters):
                break
    if len(opens)!=2:
        return grid
    (r1,c1),(r2,c2) = opens
    r_lo, r_hi = min(r1,r2), max(r1,r2)
    c_lo, c_hi = min(c1,c2), max(c1,c2)
    out = [row[:] for row in grid]
    out[r1][c1] = 4
    out[r2][c2] = 4
    for r in range(r_lo+1, r_hi):
        for c in range(c_lo+1, c_hi):
            if out[r][c]==0:
                out[r][c] = 4
    for c in range(c_lo, c_hi+1):
        if out[r1][c]==0:
            out[r1][c] = 4
    for r in range(r_lo, r_hi+1):
        if out[r][c2]==0:
            out[r][c2] = 4
    return out