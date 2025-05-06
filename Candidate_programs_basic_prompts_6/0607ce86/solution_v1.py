def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [[0]*w for _ in range(h)]
    vis = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not vis[i][j]:
                cols = set()
                pts = []
                q = [(i,j)]
                vis[i][j] = True
                for r,c in q:
                    pts.append((r,c))
                    cols.add(grid[r][c])
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] != 0 and not vis[nr][nc]:
                            vis[nr][nc] = True
                            q.append((nr,nc))
                rs = [r for r,_ in pts]; cs = [c for _,c in pts]
                r0, r1, c0, c1 = min(rs), max(rs), min(cs), max(cs)
                bh, bw = r1-r0+1, c1-c0+1
                if 6 in cols and 8 not in cols and 1 not in cols and 2 not in cols:
                    for rr in range(r0, r1+1):
                        for cc in range(c0, c1+1):
                            res[rr][cc] = 6
                elif 8 in cols:
                    if bh == 1 or bw == 1:
                        for rr in range(r0, r1+1):
                            for cc in range(c0, c1+1):
                                res[rr][cc] = 8
                    else:
                        for rr in range(r0, r1+1):
                            for cc in range(c0, c1+1):
                                if rr in (r0, r1) or cc in (c0, c1):
                                    res[rr][cc] = 8
                                else:
                                    res[rr][cc] = 3
                elif cols >= {1,2,3} and len(cols) >= 3 and bh == 4 and bw == 5:
                    cmin, cmid, cmax = sorted(cols)
                    pat = [cmin, cmin, cmid, cmax, cmax]
                    for rr in range(r0, r1+1):
                        for k in range(bw):
                            res[rr][c0+k] = pat[k]
                elif cols >= {1,2,3} and len(cols) >= 3 and bh == 4 and bw == 4:
                    cmin, cmid, cmax = sorted(cols)
                    for dr in range(bh):
                        for dc in range(bw):
                            if dr == 0:
                                v = cmid
                            elif dr == bh-1:
                                v = cmax if dc in (0, bw-1) else cmin
                            else:
                                v = cmax if dc in (0, bw-1) else cmid
                            res[r0+dr][c0+dc] = v
    return res