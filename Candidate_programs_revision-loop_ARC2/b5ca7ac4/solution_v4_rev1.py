import math
from collections import deque
def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in grid]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not vis[i][j]:
                c = grid[i][j]
                q = deque([(i,j)])
                vis[i][j] = True
                cells = []
                while q:
                    y,x = q.popleft()
                    cells.append((y,x))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < h and 0 <= nx < w and not vis[ny][nx] and grid[ny][nx]==c:
                            vis[ny][nx] = True
                            q.append((ny,nx))
                ys = [y for y,_ in cells]; xs = [x for _,x in cells]
                miny, maxy, minx, maxx = min(ys), max(ys), min(xs), max(xs)
                H, W = maxy-miny+1, maxx-minx+1
                comps.append((miny,minx,H,W,c,set((y-miny,x-minx) for y,x in cells)))
    rings = []
    squares = []
    for y,x,H,W,c,rel in comps:
        if H==W and len(rel)==4*H-4:
            rings.append((y,x,H,c,rel))
        elif H==W and len(rel)==H*H:
            squares.append((y,x,H,c,rel))
    rings.sort(); squares.sort()
    pairs = []
    for ry,rx,HL,clr,rel in rings:
        for sy,sx,HS,cs,rs in squares:
            if ry<sy and ry+HL>sy+HS-1 and rx<sx and rx+HL>sx+HS-1:
                pairs.append(((ry,rx,HL,clr,rel),(sy,sx,HS,cs,rs)))
                break
    if len(pairs)>2:
        pairs[1],pairs[2] = pairs[2],pairs[1]
    out = [[0]*w for _ in range(h)]
    side_thresh = [2,1,2,2]
    side_used = [0,0,0,0]
    for i,(ring,sq) in enumerate(pairs):
        ry,rx,L,colr,relr = ring
        sy,sx,LS,cols,rels = sq
        acc = 0
        for s,t in enumerate(side_thresh):
            if i < acc + t:
                side = s; off = i-acc; break
            acc += t
        if side==0:
            r0 = off+1; c0 = 0 if off==0 else w-L
        elif side==1:
            c0 = w-L; r0 = off+1
        elif side==2:
            r0 = h-L-off; c0 = w-L if off==0 else 0
        else:
            c0 = off+1; r0 = h-L
        path = []
        for dx in range(L):
            path.append((0,dx))
        for dy in range(1,L):
            path.append((dy,L-1))
        for dx in range(L-2,-1,-1):
            path.append((L-1,dx))
        for dy in range(L-2,0,-1):
            path.append((dy,0))
        for (dy,dx),(ry0,rx0) in zip(path, sorted(relr)):
            out[r0+dy][c0+dx] = colr
        for dy,dx in rels:
            out[r0+1+dy][c0+1+dx] = cols
    return out