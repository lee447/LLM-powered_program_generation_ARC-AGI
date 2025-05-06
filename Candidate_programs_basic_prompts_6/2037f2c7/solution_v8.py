def solve(grid):
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] and not seen[i][j]:
                q = [(i,j)]
                seen[i][j] = True
                cells = []
                mi, ma, mj, Mj = i, i, j, j
                while q:
                    x,y = q.pop()
                    cells.append((x,y))
                    mi = min(mi, x); ma = max(ma, x)
                    mj = min(mj, y); Mj = max(Mj, y)
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and grid[nx][ny] and not seen[nx][ny]:
                            seen[nx][ny] = True
                            q.append((nx,ny))
                comps.append((mi,ma,mj,Mj))
    groups = {}
    for mi,ma,mj,Mj in comps:
        ht = ma-mi+1
        groups.setdefault(ht, []).append((mi,ma,mj,Mj))
    uniq_h = sorted(groups)
    W = max(ma-mi+1 if False else (Mj-mj+1) for mi,ma,mj,Mj in comps)
    R = len(uniq_h)
    out = [[0]*W for _ in range(R)]
    for ri,ht in enumerate(uniq_h):
        xs = sorted((mj+Mj)//2 for mi,ma,mj,Mj in groups[ht])
        mn, mx = min(xs), max(xs)
        if mn==mx:
            pos = 0
        else:
            pos = 0
        out[ri][pos] = 8
        out[ri][W-1-pos] = 8
    return out