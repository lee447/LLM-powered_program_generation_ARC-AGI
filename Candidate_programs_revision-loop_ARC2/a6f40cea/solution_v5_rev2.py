from collections import deque, Counter

def solve(grid):
    h, w = len(grid), len(grid[0])
    cnt = Counter(c for row in grid for c in row)
    bg = max(cnt, key=cnt.get)
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*w for _ in range(h)]
    holes = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c != bg and not seen[i][j]:
                q = deque([(i,j)])
                seen[i][j] = True
                pts = [(i,j)]
                while q:
                    x,y = q.popleft()
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==c:
                            seen[nx][ny] = True
                            q.append((nx,ny))
                            pts.append((nx,ny))
                rs = [p[0] for p in pts]; cs = [p[1] for p in pts]
                r1,r2,c1,c2 = min(rs),max(rs),min(cs),max(cs)
                hole = False
                for rr in range(r1, r2+1):
                    for cc in range(c1, c2+1):
                        if grid[rr][cc]==bg:
                            hole = True
                            break
                    if hole: break
                holes[c] = hole
    for c,hole in holes.items():
        if hole:
            for i in range(h):
                for j in range(w):
                    if grid[i][j]==c:
                        grid[i][j]=bg
            break
    minr,minc, maxr,maxc = h,w,-1,-1
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=bg:
                minr=min(minr,i); maxr=max(maxr,i)
                minc=min(minc,j); maxc=max(maxc,j)
    if minr>maxr: return []
    return [row[minc:maxc+1] for row in grid[minr:maxr+1]]