from collections import deque, Counter
def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    cnt = Counter()
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0:
                cnt[grid[i][j]] += 1
    background = cnt.most_common(1)[0][0]
    visited0 = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    holes = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==0 and not visited0[i][j]:
                q = deque([(i,j)])
                visited0[i][j] = True
                comp = [(i,j)]
                while q:
                    x,y = q.popleft()
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not visited0[nx][ny] and grid[nx][ny]==0:
                            visited0[nx][ny]=True
                            q.append((nx,ny))
                            comp.append((nx,ny))
                xs = [x for x,y in comp]
                ys = [y for x,y in comp]
                r1, r2 = min(xs), max(xs)
                c1, c2 = min(ys), max(ys)
                if r2-r1+1>=3 and c2-c1+1>=3:
                    holes.append((r1,c1,r2,c2))
    for r1,c1,r2,c2 in holes:
        used = [[False]*w for _ in range(h)]
        for i in range(r1+1, r2):
            for j in range(c1+1, c2):
                if grid[i][j]!=0 and grid[i][j]!=background and not used[i][j]:
                    v = grid[i][j]
                    q = deque([(i,j)])
                    used[i][j] = True
                    pts = [(i,j)]
                    while q:
                        x,y = q.popleft()
                        for dx,dy in dirs:
                            nx,ny = x+dx,y+dy
                            if r1<nx<r2 and c1<ny<c2 and not used[nx][ny] and grid[nx][ny]==v:
                                used[nx][ny]=True
                                q.append((nx,ny))
                                pts.append((nx,ny))
                    cr = sum(x for x,y in pts)/len(pts)
                    cc = sum(y for x,y in pts)/len(pts)
                    corners = [(r1,c1),(r1,c2),(r2,c1),(r2,c2)]
                    br, bc = min(corners, key=lambda rc: (rc[0]-cr)**2 + (rc[1]-cc)**2)
                    if br==r1:
                        rows = [r1-1, r1]
                    else:
                        rows = [r2, r2+1]
                    if bc==c1:
                        cols = [c1-1, c1]
                    else:
                        cols = [c2, c2+1]
                    for rr in rows:
                        for cc2 in cols:
                            if 0<=rr<h and 0<=cc2<w:
                                res[rr][cc2] = v
    return res