from collections import Counter, deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    cnt = Counter(c for row in grid for c in row)
    bg = max(cnt, key=cnt.get)
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*w for _ in range(h)]
    distract = None
    for i in range(h):
        for j in range(w):
            if grid[i][j] != bg and not seen[i][j]:
                col = grid[i][j]
                q = deque([(i,j)])
                seen[i][j] = True
                pts = [(i,j)]
                while q:
                    x,y = q.popleft()
                    for dx,dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==col:
                            seen[nx][ny] = True
                            q.append((nx,ny))
                            pts.append((nx,ny))
                for x,y in pts:
                    deg = 0
                    for dx,dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and grid[nx][ny]==col:
                            deg += 1
                    if deg == 4:
                        distract = col
                        break
                if distract is not None:
                    break
        if distract is not None:
            break
    if distract is not None:
        for i in range(h):
            for j in range(w):
                if grid[i][j] == distract:
                    grid[i][j] = bg
    minr, minc, maxr, maxc = h, w, -1, -1
    for i in range(h):
        for j in range(w):
            if grid[i][j] != bg:
                minr = min(minr, i)
                maxr = max(maxr, i)
                minc = min(minc, j)
                maxc = max(maxc, j)
    if minr > maxr:
        return []
    return [row[minc:maxc+1] for row in grid[minr:maxr+1]]