from typing import List, Tuple

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 2 and not visited[y][x]:
                stack = [(y,x)]
                visited[y][x] = True
                pts = []
                while stack:
                    cy, cx = stack.pop()
                    pts.append((cy,cx))
                    for dy,dx in dirs:
                        ny,nx = cy+dy, cx+dx
                        if 0<=ny<h and 0<=nx<w and not visited[ny][nx] and grid[ny][nx]==2:
                            visited[ny][nx] = True
                            stack.append((ny,nx))
                ys = [p[0] for p in pts]; xs = [p[1] for p in pts]
                ymin,ymax = min(ys), max(ys)
                xmin,xmax = min(xs), max(xs)
                if ymax-ymin==3 and xmax-xmin==3:
                    comps.append((ymin, xmin, pts))
    comps.sort(key=lambda t:(t[0],t[1]))
    palette = [2,8,3]
    out = [row[:] for row in grid]
    for i,(_,_,pts) in enumerate(comps):
        tier = i//2
        left = (i%2)==0
        c = palette[(tier + (0 if left else 1))%3]
        for y,x in pts:
            out[y][x] = c
    return out