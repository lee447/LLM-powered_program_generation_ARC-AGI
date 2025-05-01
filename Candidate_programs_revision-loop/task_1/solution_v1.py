def solve(grid):
    from collections import deque, defaultdict
    n, m = len(grid), len(grid[0])
    vis = [[False]*m for _ in range(n)]
    comps = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0 and not vis[i][j]:
                q = deque([(i,j)])
                vis[i][j] = True
                cells = []
                while q:
                    x,y = q.popleft()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<n and 0<=ny<m and grid[nx][ny]!=0 and not vis[nx][ny]:
                            vis[nx][ny] = True
                            q.append((nx,ny))
                comps.append(cells)
    dims2comps = defaultdict(list)
    intact = defaultdict(list)
    for cells in comps:
        rs = [x for x,y in cells]
        cs = [y for x,y in cells]
        r0, r1 = min(rs), max(rs)
        c0, c1 = min(cs), max(cs)
        h, w = r1-r0+1, c1-c0+1
        if h*w <= 3: continue
        dims2comps[(h,w)].append((r0,c0,cells))
        ok = True
        for ii in range(r0, r0+h):
            for jj in range(c0, c0+w):
                if grid[ii][jj] == 0:
                    ok = False
                    break
            if not ok: break
        if ok:
            intact[(h,w)].append((r0,c0))
    prototypes = {}
    for d, lst in intact.items():
        if len(lst) >= 1 and len(dims2comps[d]) > 1:
            h,w = d
            r0,c0 = lst[0]
            pat = [row[c0:c0+w] for row in grid[r0:r0+h]]
            prototypes[d] = pat
    out = [[0]*m for _ in range(n)]
    for d, lst in dims2comps.items():
        if d in prototypes:
            h,w = d
            for r0,c0,_ in lst:
                for di in range(h):
                    for dj in range(w):
                        out[r0+di][c0+dj] = prototypes[d][di][dj]
    return out