from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    comps = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 1 and not vis[y][x]:
                stack = [(y, x)]
                vis[y][x] = True
                coords = []
                miny = maxy = y
                minx = maxx = x
                while stack:
                    cy, cx = stack.pop()
                    coords.append((cy, cx))
                    miny = min(miny, cy)
                    maxy = max(maxy, cy)
                    minx = min(minx, cx)
                    maxx = max(maxx, cx)
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = cy+dy, cx+dx
                        if 0<=ny<h and 0<=nx<w and not vis[ny][nx] and grid[ny][nx] == 1:
                            vis[ny][nx] = True
                            stack.append((ny, nx))
                comps.append((miny, minx, maxy, maxx))
    out = [row[:] for row in grid]
    mapping = {1: 2, 2: 8, 3: 6}
    for miny, minx, maxy, maxx in comps:
        size_y = maxy-miny+1
        size_x = maxx-minx+1
        rings = min(size_y//2, size_x//2, 3)
        for y in range(miny-rings, maxy+rings+1):
            if y<0 or y>=h: continue
            for x in range(minx-rings, maxx+rings+1):
                if x<0 or x>=w: continue
                dx = 0 if minx<=x<=maxx else (minx-x if x<minx else x-maxx)
                dy = 0 if miny<=y<=maxy else (miny-y if y<miny else y-maxy)
                d = max(dx, dy)
                if 1 <= d <= rings:
                    out[y][x] = mapping[d]
    return out