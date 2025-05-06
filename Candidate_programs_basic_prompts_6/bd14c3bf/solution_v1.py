def solve(grid):
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in grid]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def comp(i,j):
        pts = [(i,j)]
        seen[i][j] = True
        q = [(i,j)]
        while q:
            x,y = q.pop()
            for dx,dy in dirs:
                nx,ny = x+dx, y+dy
                if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==1:
                    seen[nx][ny]=True
                    pts.append((nx,ny))
                    q.append((nx,ny))
        return pts
    res = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not seen[i][j]:
                P = comp(i,j)
                xs = [x for x,y in P]; ys = [y for x,y in P]
                xmin,xmax = min(xs), max(xs)
                ymin,ymax = min(ys), max(ys)
                bw, bh = ymax-ymin+1, xmax-xmin+1
                full = len(P)==bw*bh
                long = bw>=4 or bh>=4
                if full or long:
                    for x,y in P:
                        res[x][y]=2
    return res