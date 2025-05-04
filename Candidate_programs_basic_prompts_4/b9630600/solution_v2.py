def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    rects = []
    for r in range(h):
        for c in range(w):
            if grid[r][c]==3 and not vis[r][c]:
                stack=[(r,c)]
                vis[r][c]=True
                r0,r1,c0,c1 = r,r,c,c
                while stack:
                    y,x = stack.pop()
                    r0,r1,c0,c1 = min(r0,y),max(r1,y),min(c0,x),max(c1,x)
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx = y+dy, x+dx
                        if 0<=ny<h and 0<=nx<w and grid[ny][nx]==3 and not vis[ny][nx]:
                            vis[ny][nx]=True
                            stack.append((ny,nx))
                if r1-r0>=2 and c1-c0>=2:
                    rects.append((r0,r1,c0,c1))
    bands = {}
    for r0,r1,c0,c1 in rects:
        bands.setdefault((r0,r1), []).append((c0,c1))
    for (r0,r1), L in bands.items():
        L.sort()
        n = len(L)
        for i,(c0,c1) in enumerate(L):
            rows = (r0+1, r1-1)
            if n>1:
                if i>0:
                    pc0,pc1 = L[i-1]
                    for rr in rows:
                        for cc in range(pc1, c0+1):
                            grid[rr][cc]=3
                if i<n-1:
                    nc0,nc1 = L[i+1]
                    for rr in rows:
                        for cc in range(c1, nc0+1):
                            grid[rr][cc]=3
            else:
                wdt = c1-c0+1
                k = wdt//2
                for rr in rows:
                    for t in range(k):
                        grid[rr][c0+t]=3
                        grid[rr][c1-t]=3
    return grid