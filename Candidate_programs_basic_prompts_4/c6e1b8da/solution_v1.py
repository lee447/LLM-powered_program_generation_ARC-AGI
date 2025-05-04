def solve(grid):
    H, W = len(grid), len(grid[0])
    from collections import defaultdict, deque
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*W for _ in range(H)]
    rects = []
    for i in range(H):
        for j in range(W):
            c = grid[i][j]
            if c and not seen[i][j]:
                q = deque([(i,j)])
                seen[i][j] = True
                pts = []
                while q:
                    x,y = q.popleft()
                    pts.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and not seen[nx][ny] and grid[nx][ny]==c:
                            seen[nx][ny] = True
                            q.append((nx,ny))
                rs = [p[0] for p in pts]
                cs = [p[1] for p in pts]
                r0,r1 = min(rs), max(rs)
                c0,c1 = min(cs), max(cs)
                rects.append((r0, c0, r1, c1, c, pts))
    rects.sort(key=lambda x: x[0])
    out = [[0]*W for _ in range(H)]
    x = 0
    for r0,c0,r1,c1,c,pts in rects:
        h = r1-r0+1
        w = c1-c0+1
        dx = x - c0
        for i in range(r0, r0+h):
            for j in range(c0, c0+w):
                out[i][j+dx] = c
        x += w+1
    return out