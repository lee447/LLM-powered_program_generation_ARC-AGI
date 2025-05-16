def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    from collections import deque, Counter
    # find background color
    cnt = Counter()
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0:
                cnt[grid[i][j]] += 1
    background = cnt.most_common(1)[0][0]
    visited = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==0 and not visited[i][j]:
                q = deque([(i,j)])
                visited[i][j] = True
                comp = [(i,j)]
                while q:
                    x,y = q.popleft()
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==0:
                            visited[nx][ny]=True
                            q.append((nx,ny))
                            comp.append((nx,ny))
                xs = [x for x,y in comp]
                ys = [y for x,y in comp]
                r1, r2 = min(xs), max(xs)
                c1, c2 = min(ys), max(ys)
                if r2-r1+1>=3 and c2-c1+1>=3:
                    comps.append((r1,c1,r2,c2))
    for r1,c1,r2,c2 in comps:
        cr = (r1+r2)/2.0
        cc = (c1+c2)/2.0
        for i in range(r1+1, r2):
            for j in range(c1+1, c2):
                v = grid[i][j]
                if v!=0 and v!=background:
                    top = i<cr
                    left = j<cc
                    if top and left:
                        br, bc = r1-1, c1-1
                    elif top and not left:
                        br, bc = r1-1, c2
                    elif not top and left:
                        br, bc = r2, c1-1
                    else:
                        br, bc = r2, c2
                    if br<0 or bc<0 or br+1>=h or bc+1>=w:
                        br, bc = r1-1, c1-1
                    for di in (0,1):
                        for dj in (0,1):
                            res[br+di][bc+dj] = v
    return res