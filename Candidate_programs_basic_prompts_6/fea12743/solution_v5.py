from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    g = [row[:] for row in grid]
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not vis[i][j]:
                pts, stack = [], [(i,j)]
                vis[i][j] = True
                while stack:
                    x,y = stack.pop()
                    pts.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and grid[nx][ny]!=0 and not vis[nx][ny]:
                            vis[nx][ny]=True
                            stack.append((nx,ny))
                comps.append(pts)
    # determine block rows by avg x
    centers = [sum(x for x,y in pts)/len(pts) for pts in comps]
    order = sorted(range(len(comps)), key=lambda k:(centers[k], min(y for x,y in comps[k])))
    colors = {}
    next_new = [8,3,2]
    ni = 0
    for idx in order:
        br = int(centers[idx]//(h/4))
        pos = 0 if min(y for x,y in comps[idx])<w/2 else 1
        if br==0:
            if pos==0:
                colors[idx] = 2
            else:
                colors[idx] = 8
        elif br==1:
            if pos==0:
                colors[idx] = 8
            else:
                colors[idx] = 3
        else:
            if pos==0:
                colors[idx] = 2
            else:
                colors[idx] = 2
    for k,pts in enumerate(comps):
        for x,y in pts:
            g[x][y] = colors[k]
    return g