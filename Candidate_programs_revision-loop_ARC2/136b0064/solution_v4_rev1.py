from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    for bx in range(w):
        if all(grid[y][bx] == 4 for y in range(h)):
            bar = bx
            break
    left_w = bar
    vis = [[False] * left_w for _ in range(h)]
    comps = []
    for y in range(h):
        for x in range(left_w):
            c = grid[y][x]
            if c not in (0, 4) and not vis[y][x]:
                pts = [(y, x)]
                vis[y][x] = True
                stack = [(y, x)]
                while stack:
                    yy, xx = stack.pop()
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = yy + dy, xx + dx
                        if 0 <= ny < h and 0 <= nx < left_w and not vis[ny][nx] and grid[ny][nx] == c:
                            vis[ny][nx] = True
                            pts.append((ny, nx))
                            stack.append((ny, nx))
                ys = [p[0] for p in pts]
                xs = [p[1] for p in pts]
                block = min(ys) // 4
                comps.append((block, min(xs), c, pts))
    comps.sort(key=lambda t: (t[0], t[1], t[2]))
    out = [[0] * left_w for _ in range(h)]
    r = 0
    for block, _, c, pts in comps:
        ys = [p[0] for p in pts]
        xs = [p[1] for p in pts]
        miny, minx = min(ys), min(xs)
        wbox = max(xs) - minx + 1
        hbox = max(ys) - miny + 1
        if wbox > hbox:
            if r < h:
                for i in range(wbox):
                    if minx + i < left_w:
                        out[r][minx + i] = c
                r += 1
        else:
            if r + hbox <= h:
                for i in range(hbox):
                    out[r + i][minx] = c
                r += hbox
    return out