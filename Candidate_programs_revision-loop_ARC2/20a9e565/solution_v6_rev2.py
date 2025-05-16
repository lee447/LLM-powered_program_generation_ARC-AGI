from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[False]*w for _ in range(h)]
    comp_count = {}
    comp_size = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c!=0 and not visited[i][j]:
                comp_count.setdefault(c,0)
                comp_count[c]+=1
                size = 0
                dq = deque([(i,j)])
                visited[i][j]=True
                while dq:
                    x,y = dq.popleft()
                    size += 1
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==c:
                            visited[nx][ny]=True
                            dq.append((nx,ny))
                comp_size[c] = comp_size.get(c,0) + size
    big = [c for c in comp_count if comp_count[c]>2]
    if big:
        target = max(big, key=lambda c: comp_count[c])
    else:
        target = min(comp_count, key=lambda c: (comp_count[c], comp_size[c]))
    rows = [i for i in range(h) for j in range(w) if grid[i][j]==target]
    cols = [j for i in range(h) for j in range(w) if grid[i][j]==target]
    r0,r1 = min(rows), max(rows)
    c0,c1 = min(cols), max(cols)
    crop = [row[c0:c1+1] for row in grid[r0:r1+1]]
    nr = [r for r in crop if any(v!=0 for v in r)]
    if not nr:
        return []
    m,n = len(nr), len(nr[0])
    keep = [any(nr[i][j]!=0 for i in range(m)) for j in range(n)]
    out = [[nr[i][j] for j in range(n) if keep[j]] for i in range(m)]
    return out