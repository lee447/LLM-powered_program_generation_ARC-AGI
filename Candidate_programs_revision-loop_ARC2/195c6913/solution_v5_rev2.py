import collections, math
from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    per = []
    for j in range(w):
        per.append(grid[0][j])
        per.append(grid[h-1][j])
    for i in range(h):
        per.append(grid[i][0])
        per.append(grid[i][w-1])
    cnt = collections.Counter(per)
    frame_color = cnt.most_common(1)[0][0]
    bg_cnt = {c:cnt for c,cnt in cnt.items() if c!=frame_color}
    bg_color = max(bg_cnt, key=bg_cnt.get)
    outside = [[False]*w for _ in range(h)]
    dq = deque()
    for i in range(h):
        for j in (0, w-1):
            if grid[i][j]==bg_color:
                outside[i][j]=True
                dq.append((i,j))
    for j in range(w):
        for i in (0, h-1):
            if grid[i][j]==bg_color and not outside[i][j]:
                outside[i][j]=True
                dq.append((i,j))
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while dq:
        x,y = dq.popleft()
        for dx,dy in dirs:
            nx,ny = x+dx, y+dy
            if 0<=nx<h and 0<=ny<w and not outside[nx][ny] and grid[nx][ny]==bg_color:
                outside[nx][ny] = True
                dq.append((nx,ny))
    mask = [[not outside[i][j] and grid[i][j]!=frame_color and grid[i][j]!=bg_color for j in range(w)] for i in range(h)]
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if mask[i][j] and not seen[i][j]:
                c0 = grid[i][j]
                dq = deque()
                dq.append((i,j))
                seen[i][j]=True
                comp=[]
                while dq:
                    x,y = dq.popleft()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and mask[nx][ny] and grid[nx][ny]==c0:
                            seen[nx][ny]=True
                            dq.append((nx,ny))
                comps.append(comp)
    uniq = []
    sigset = set()
    for comp in comps:
        cells = sorted(comp)
        rr = min(x for x,y in cells)
        cc = min(y for x,y in cells)
        offs = tuple((x-rr,y-cc) for x,y in cells)
        clrs = tuple(grid[x][y] for x,y in cells)
        sig = (offs,clrs)
        if sig not in sigset:
            sigset.add(sig)
            uniq.append(sig)
    shapes = sorted(uniq, key=lambda oc:oc[1])
    S = int(math.sqrt(len(shapes[0][0])))
    places = []
    for i in range(h-S+1):
        for j in range(w-S+1):
            ok = True
            for dr,dc in shapes[0][0]:
                if grid[i+dr][j+dc]==frame_color:
                    ok=False; break
            if ok:
                places.append((i,j))
    out = [row[:] for row in grid]
    for idx,(r,c) in enumerate(sorted(places)):
        offs,clrs = shapes[idx%len(shapes)]
        for (dr,dc),clr in zip(offs,clrs):
            out[r+dr][c+dc] = clr
    return out