from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    # flood‐fill components
    vis = [[False]*w for _ in range(h)]
    comps = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c!=0 and not vis[i][j]:
                stack = [(i,j)]
                vis[i][j] = True
                pts = []
                while stack:
                    x,y = stack.pop()
                    pts.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==c:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                comps.setdefault(c,[]).append(pts)
    # bresenham
    def bres(a: Tuple[int,int], b: Tuple[int,int]) -> List[Tuple[int,int]]:
        x1,y1 = a; x2,y2 = b
        dx,dy = abs(x2-x1), abs(y2-y1)
        sx = 1 if x2>=x1 else -1
        sy = 1 if y2>=y1 else -1
        pts = []
        if dx>=dy:
            err = dx//2
            y = y1
            for x in range(x1, x2+sx, sx):
                pts.append((x,y))
                err -= dy
                if err<0:
                    y += sy
                    err += dx
        else:
            err = dy//2
            x = x1
            for y in range(y1, y2+sy, sy):
                pts.append((x,y))
                err -= dx
                if err<0:
                    x += sx
                    err += dy
        return pts
    out = [[0]*w for _ in range(h)]
    for c, groups in comps.items():
        if len(groups)==1:
            for x,y in groups[0]:
                out[x][y] = c
            continue
        # sort clusters by minimal reading order
        groups.sort(key=lambda pts: (min(p[0] for p in pts), min(p[1] for p in pts)))
        # build chain
        chain = []
        for k in range(len(groups)-1):
            a = groups[k]
            b = groups[k+1]
            # pick nearest pair
            best = None; bd = None
            for p in a:
                for q in b:
                    d = max(abs(p[0]-q[0]), abs(p[1]-q[1]))
                    if bd is None or d<bd:
                        bd = d; best = (p,q)
            seg = bres(best[0], best[1])
            if k==0:
                chain += seg
            else:
                chain += seg[1:]
        # draw chain
        for x,y in chain:
            if 0<=x<h and 0<=y<w:
                out[x][y] = c
    return out