import numpy as np

def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    comps = {}
    dirs8 = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c and not vis[i][j]:
                stack = [(i,j)]
                vis[i][j] = True
                lst = []
                while stack:
                    x,y = stack.pop()
                    lst.append((x,y))
                    for dx,dy in dirs8:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==c:
                            vis[nx][ny]=True
                            stack.append((nx,ny))
                comps.setdefault(c, []).append(lst)
    out = [row[:] for row in grid]
    def sign(x): return 1 if x>0 else -1 if x<0 else 0
    for c, clist in comps.items():
        pts = sum(clist,[])
        if len(clist)==2:
            # pick global extremes
            p1 = min(pts, key=lambda p:p[0]+p[1])
            p2 = max(pts, key=lambda p:p[0]+p[1])
        else:
            # one group: take the two farthest apart
            best = (0,None,None)
            for a in pts:
                for b in pts:
                    d = (a[0]-b[0])**2+(a[1]-b[1])**2
                    if d>best[0]:
                        best = (d,a,b)
            p1,p2 = best[1],best[2]
        dr,dc = sign(p2[0]-p1[0]), sign(p2[1]-p1[1])
        # draw between p1 and p2
        x,y = p1
        while True:
            out[x][y] = c
            if (x,y)==p2: break
            x+=dr; y+=dc
        # extend backward
        x,y = p1
        while 0<=x-dr<h and 0<=y-dc<w:
            x-=dr; y-=dc
            out[x][y]=c
        # extend forward
        x,y = p2
        while 0<=x+dr<h and 0<=y+dc<w:
            x+=dr; y+=dc
            out[x][y]=c
    return out