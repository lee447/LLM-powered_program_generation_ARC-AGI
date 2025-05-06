def solve(grid):
    from collections import deque
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in grid]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not seen[i][j]:
                color = grid[i][j]
                q = deque([(i,j)])
                seen[i][j] = True
                pts = []
                while q:
                    x,y = q.popleft()
                    pts.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==color:
                            seen[nx][ny] = True
                            q.append((nx,ny))
                minx = min(p[0] for p in pts)
                maxx = max(p[0] for p in pts)
                miny = min(p[1] for p in pts)
                maxy = max(p[1] for p in pts)
                comps.append((len(pts),minx,maxx,miny,maxy))
    comps.sort(reverse=True)
    _, a,b,c,d = comps[0]
    sub = [row[c:d+1] for row in grid[a:b+1]]
    H, W = len(sub), len(sub[0])
    out_h = H//2
    out = [[0]*W for _ in range(out_h)]
    for i in range(out_h):
        for j in range(W):
            if (sub[i][j]==0 and sub[H-1-i][j]==0):
                out[i][j] = 8
    return out