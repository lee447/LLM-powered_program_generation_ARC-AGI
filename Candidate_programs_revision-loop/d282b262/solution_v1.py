def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] and not vis[i][j]:
                pts = [(i,j)]
                vis[i][j] = True
                q = [(i,j)]
                for x,y in q:
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and grid[nx][ny] and not vis[nx][ny]:
                            vis[nx][ny] = True
                            q.append((nx,ny))
                            pts.append((nx,ny))
                rs = [p[0] for p in pts]; cs = [p[1] for p in pts]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                pat = [[grid[r][c] for c in range(c0, c1+1)] for r in range(r0, r1+1)]
                clusters.append((r0, c0, pat))
    out = [[0]*w for _ in range(h)]
    for r in range(h):
        segs = []
        for r0,c0,pat in clusters:
            if r0 <= r < r0+len(pat):
                segs.append((c0, pat[r-r0]))
        segs.sort(key=lambda x:x[0])
        total = sum(len(s) for _,s in segs)
        pos = w-total
        for _,s in segs:
            for v in s:
                out[r][pos] = v
                pos += 1
    return out