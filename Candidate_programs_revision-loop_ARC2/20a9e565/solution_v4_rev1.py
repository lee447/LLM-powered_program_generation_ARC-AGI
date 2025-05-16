from collections import deque
def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    # find connected-component counts for each color
    visited = [[False]*w for _ in range(h)]
    comp_count = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c and not visited[i][j]:
                comp_count.setdefault(c,0)
                comp_count[c] += 1
                dq = deque([(i,j)])
                visited[i][j] = True
                while dq:
                    x,y = dq.popleft()
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==c:
                            visited[nx][ny] = True
                            dq.append((nx,ny))
    # pick color with most components
    target = max(comp_count, key=lambda c: comp_count[c])
    # bounding box of that color
    rows = [i for i in range(h) for j in range(w) if grid[i][j]==target]
    cols = [j for i in range(h) for j in range(w) if grid[i][j]==target]
    r0, r1 = min(rows), max(rows)
    c0, c1 = min(cols), max(cols)
    # crop & mask
    crop = [[grid[i][j] if grid[i][j]==target else 0 for j in range(c0,c1+1)] for i in range(r0,r1+1)]
    # remove zero rows
    nr = [row for row in crop if any(v!=0 for v in row)]
    if not nr:
        return []
    # remove zero columns
    m, n = len(nr), len(nr[0])
    keep = [any(nr[i][j]!=0 for i in range(m)) for j in range(n)]
    out = [[nr[i][j] for j in range(n) if keep[j]] for i in range(m)]
    return out