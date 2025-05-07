from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    markers = [(i, j) for i in range(h) for j in range(w) if grid[i][j] not in (0, 1)]
    if not markers:
        return grid
    minr = min(i for i, j in markers)
    maxr = max(i for i, j in markers)
    minc = min(j for i, j in markers)
    maxc = max(j for i, j in markers)
    pattern = [row[minc:maxc+1] for row in grid[minr:maxr+1]]
    pr, pc = len(pattern), len(pattern[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not seen[i][j]:
                q = deque([(i, j)])
                seen[i][j] = True
                pts = []
                while q:
                    x, y = q.popleft()
                    pts.append((x, y))
                    for dx, dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not seen[nx][ny] and grid[nx][ny] == 1:
                            seen[nx][ny] = True
                            q.append((nx, ny))
                comps.append(pts)
    centers = []
    for pts in comps:
        cx = sum(x for x, y in pts)/len(pts)
        cy = sum(y for x, y in pts)/len(pts)
        centers.append((cx, cy))
    mincx = min(cx for cx, cy in centers)
    maxcx = max(cx for cx, cy in centers)
    mincy = min(cy for cx, cy in centers)
    maxcy = max(cy for cx, cy in centers)
    out = [row[:] for row in grid]
    for pts, (cx, cy) in zip(comps, centers):
        if maxcx > mincx:
            i = int(round((cx - mincx)/(maxcx - mincx)*(pr-1)))
        else:
            i = 0
        if maxcy > mincy:
            j = int(round((cy - mincy)/(maxcy - mincy)*(pc-1)))
        else:
            j = 0
        col = pattern[i][j]
        for x, y in pts:
            out[x][y] = col
    return out