from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    uniform_cols = [c for c in range(w) if all(grid[r][c] == grid[0][c] for r in range(h))]
    uniform_rows = [r for r in range(h) if all(grid[r][c] == grid[r][0] for c in range(w))]

    def bfs_color(x0, y0, xmin, xmax, ymin, ymax, seen, bg):
        q = deque([(x0, y0)])
        comp = []
        while q:
            x, y = q.popleft()
            if (x, y) in seen or not (xmin <= x <= xmax and ymin <= y <= ymax):
                continue
            if grid[y][x] == bg:
                continue
            seen.add((x, y))
            comp.append((x, y))
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                q.append((x+dx, y+dy))
        return comp

    if len(uniform_cols) >= 2:
        # vertical case
        by_color = {}
        for c in uniform_cols:
            colv = grid[0][c]
            by_color.setdefault(colv, []).append(c)
        best = ( -1, None )
        for colv, lst in by_color.items():
            if len(lst) >= 2:
                mn, mx = min(lst), max(lst)
                gap = mx - mn - 1
                if gap > best[0]:
                    best = (gap, (mn, mx, colv))
        _, (c0, c1, border) = best
        bg = grid[0][c0+1]
        region_w = c1 - c0 - 1
        out = [[border]*(region_w+2) for _ in range(h)]
        seen = set()
        comps = []
        for y in range(h):
            for x in range(c1+1, w):
                if (x,y) not in seen and grid[y][x] not in (bg, border):
                    comp = bfs_color(x, y, c1+1, w-1, 0, h-1, seen, bg)
                    xs = [p[0] for p in comp]; ys = [p[1] for p in comp]
                    comps.append((min(ys), min(xs), max(ys)-min(ys)+1, max(xs)-min(xs)+1, comp))
        comps.sort(key=lambda t: (t[0], t[1]))
        cur_y = 0
        for miny, minx, hh, ww, comp in comps:
            off_x = (region_w - ww)//2
            for x,y in comp:
                out[cur_y + (y-miny)][1 + off_x + (x-minx)] = grid[y][x]
            cur_y += hh
        return out
    else:
        # horizontal case
        by_color = {}
        for r in uniform_rows:
            rv = grid[r][0]
            by_color.setdefault(rv, []).append(r)
        best = (-1, None)
        for rv, lst in by_color.items():
            if len(lst) >= 2:
                mn, mx = min(lst), max(lst)
                gap = mx - mn - 1
                if gap > best[0]:
                    best = (gap, (mn, mx, rv))
        _, (r0, r1, _) = best
        region_h = r1 - r0 - 1
        bg = grid[r0+1][0]
        border = grid[r1+1][0]
        out = [[border]*w for _ in range(region_h)]
        seen = set()
        comps = []
        for y in range(r0+1, r1):
            for x in range(w):
                if (x,y) not in seen and grid[y][x] != bg:
                    comp = bfs_color(x, y, 0, w-1, r0+1, r1-1, seen, bg)
                    xs = [p[0] for p in comp]; ys = [p[1] for p in comp]
                    comps.append((min(xs), min(ys), max(xs)-min(xs)+1, max(ys)-min(ys)+1, comp))
        comps.sort(key=lambda t: (t[0], t[1]))
        cur_x = 0
        for minx, miny, ww, hh, comp in comps:
            off_y = (region_h - hh)//2
            for x,y in comp:
                out[off_y + (y-miny)][cur_x + (x-minx)] = grid[y][x]
            cur_x += ww
        return out