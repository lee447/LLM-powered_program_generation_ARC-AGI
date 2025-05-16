from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bar = next(x for x in range(w) if all(grid[y][x] == 4 for y in range(h)))
    left_w = bar
    right_x = bar + 1
    def extract(g, ox):
        H, W = len(g), len(g[0])
        vis = [[False]*W for _ in range(H)]
        comps = []
        for y in range(H):
            for x in range(W):
                c = g[y][x]
                if c not in (0,4) and not vis[y][x]:
                    pts = [(y, x)]
                    vis[y][x] = True
                    stack = [(y, x)]
                    while stack:
                        yy, xx = stack.pop()
                        for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                            ny, nx = yy+dy, xx+dx
                            if 0 <= ny < H and 0 <= nx < W and not vis[ny][nx] and g[ny][nx] == c:
                                vis[ny][nx] = True
                                pts.append((ny, nx))
                                stack.append((ny, nx))
                    ys = [p[0] for p in pts]
                    xs = [p[1] for p in pts]
                    block = min(ys)//4
                    comps.append((block, min(xs)+ox, c, pts))
        return comps
    comps = extract([row[:left_w] for row in grid], 0) + extract([row[right_x:] for row in grid], right_x)
    comps.sort(key=lambda t: (t[0], t[1], t[2]))
    out = [[0]*left_w for _ in range(h)]
    r = 0
    for block, mx, c, pts in comps:
        xs = [p[1] for p in pts]
        ys = [p[0] for p in pts]
        minx, miny = min(xs), min(ys)
        wbox = max(xs) - minx + 1
        hbox = max(ys) - miny + 1
        if wbox >= hbox:
            if r < h:
                for i in range(wbox):
                    x0 = minx + i
                    if x0 < left_w:
                        out[r][x0] = c
                r += 1
        else:
            if r + hbox <= h:
                for i in range(hbox):
                    y0 = r + i
                    out[y0][minx] = c
                r += hbox
    return out