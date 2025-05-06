def solve(grid):
    h, w = len(grid), len(grid[0])
    def find_cluster(val):
        seen = [[False]*w for _ in range(h)]
        clusters = []
        for i in range(h):
            for j in range(w):
                if grid[i][j]==val and not seen[i][j]:
                    stack = [(i,j)]
                    seen[i][j]=True
                    pts=[]
                    while stack:
                        x,y = stack.pop()
                        pts.append((x,y))
                        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                            nx,ny = x+dx,y+dy
                            if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==val:
                                seen[nx][ny]=True
                                stack.append((nx,ny))
                    clusters.append(pts)
        return clusters
    c3 = find_cluster(3)
    c3 = sorted(c3, key=lambda pts: min(x for x,y in pts))
    pts = c3[0]
    rows = sorted({x for x,y in pts})
    cols = sorted({y for x,y in pts})
    cnt2 = [r for r in rows if sum(1 for x,y in pts if x==r)==2]
    cnt4 = [r for r in rows if sum(1 for x,y in pts if x==r)==4]
    r_top, r_bot = cnt2[0], cnt2[-1]
    rc = [r for r in cnt4 if r<r_top]
    if rc: r_ctr=rc[-1]
    else: r_ctr=cnt4[0]
    cmin, cmax = min(y for x,y in pts if x==r_ctr), max(y for x,y in pts if x==r_ctr)
    out = []
    for r in [r_top, r_ctr, r_bot]:
        row = []
        for c in range(cmin, cmax+1):
            row.append(8 if grid[r][c]==3 else 0)
        out.append(row)
    return out