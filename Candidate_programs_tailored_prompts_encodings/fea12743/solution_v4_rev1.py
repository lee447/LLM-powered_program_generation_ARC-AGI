import collections

def solve(grid):
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 2 and not seen[i][j]:
                q = collections.deque([(i,j)])
                seen[i][j] = True
                pts = []
                while q:
                    x,y = q.popleft()
                    pts.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx,y+dy
                        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny]==2 and not seen[nx][ny]:
                            seen[nx][ny] = True
                            q.append((nx,ny))
                clusters.append(pts)
    clusters.sort(key=len, reverse=True)
    out = [row[:] for row in grid]
    for idx, pts in enumerate(clusters[:3]):
        color = 3 if idx == 0 else 8
        for x,y in pts:
            out[x][y] = color
    return out