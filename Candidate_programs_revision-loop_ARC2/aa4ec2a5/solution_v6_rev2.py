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
                miny = maxy = y
                minx = maxx = x
                while stack:
                    cy, cx = stack.pop()
                    miny = min(miny, cy); maxy = max(maxy, cy)
                    minx = min(minx, cx); maxx = max(maxx, cx)
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = cy+dy, cx+dx
                        if 0 <= ny < h and 0 <= nx < w and not vis[ny][nx] and grid[ny][nx] == 1:
                            vis[ny][nx] = True
                            stack.append((ny, nx))
                comps.append((miny, minx, maxy, maxx))
    out = [row[:] for row in grid]
    mapping = {1: 2, 2: 8, 3: 6}
    for miny, minx, maxy, maxx in comps:
        size_y = maxy - miny + 1
        size_x = maxx - minx + 1
        rings = min(size_y//2, size_x//2, 3)
        for d in range(1, rings+1):
            y0, y1 = max(0, miny-d), min(h-1, maxy+d)
            x0, x1 = max(0, minx-d), min(w-1, maxx+d)
            for yy in range(y0, y1+1):
                for xx in range(x0, x1+1):
                    dx = 0 if minx <= xx <= maxx else (minx-xx if xx < minx else xx-maxx)
                    dy = 0 if miny <= yy <= maxy else (miny-yy if yy < miny else yy-maxy)
                    if max(dx, dy) == d and grid[yy][xx] == 4:
                        out[yy][xx] = mapping[d]
    return out
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
                miny = maxy = y
                minx = maxx = x
                while stack:
                    cy, cx = stack.pop()
                    miny = min(miny, cy); maxy = max(maxy, cy)
                    minx = min(minx, cx); maxx = max(maxx, cx)
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = cy+dy, cx+dx
                        if 0 <= ny < h and 0 <= nx < w and not vis[ny][nx] and grid[ny][nx] == 1:
                            vis[ny][nx] = True
                            stack.append((ny, nx))
                comps.append((miny, minx, maxy, maxx))
    out = [row[:] for row in grid]
    mapping = {1: 2, 2: 8, 3: 6}
    for miny, minx, maxy, maxx in comps:
        size_y = maxy - miny + 1
        size_x = maxx - minx + 1
        rings = min(size_y//2, size_x//2, 3)
        for d in range(1, rings+1):
            y0, y1 = max(0, miny-d), min(h-1, maxy+d)
            x0, x1 = max(0, minx-d), min(w-1, maxx+d)
            for yy in range(y0, y1+1):
                for xx in range(x0, x1+1):
                    dx = 0 if minx <= xx <= maxx else (minx-xx if xx < minx else xx-maxx)
                    dy = 0 if miny <= yy <= maxy else (miny-yy if yy < miny else yy-maxy)
                    if max(dx, dy) == d and grid[yy][xx] == 4:
                        out[yy][xx] = mapping[d]
    return out