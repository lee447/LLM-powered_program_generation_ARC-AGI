def solve(grid):
    from collections import deque
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    clusters = []
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c!=0 and not seen[i][j]:
                q = deque([(i,j)])
                seen[i][j] = True
                cells = []
                while q:
                    x,y = q.popleft()
                    cells.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==c:
                            seen[nx][ny] = True
                            q.append((nx,ny))
                rs = [x for x,_ in cells]
                cs = [y for _,y in cells]
                r0,r1,minc,maxc = min(rs), max(rs), min(cs), max(cs)
                clusters.append((r0, minc, r1, maxc, c, set(cells)))
    # pick the cluster whose topmost cell is smallest row, then smallest col
    clusters.sort(key=lambda x:(x[0], x[1]))
    r0, c0, r1, c1, col, cells = clusters[0]
    H, W = r1-r0+1, c1-c0+1
    ans = [[0]*W for _ in range(H)]
    for x,y in cells:
        ans[x-r0][y-c0] = col
    return ans