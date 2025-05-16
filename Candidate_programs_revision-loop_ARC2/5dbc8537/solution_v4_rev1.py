from typing import List, Tuple
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    uniform_rows = [r for r in range(h) if len({grid[r][c] for c in range(w)}) == 1]
    uniform_cols = [c for c in range(w) if len({grid[r][c] for r in range(h)}) == 1]
    def bfs(x0, y0, col, xmin, xmax, ymin, ymax, seen):
        q = deque([(x0, y0)])
        comp = []
        while q:
            x, y = q.popleft()
            if (x, y) in seen: continue
            if grid[y][x] != col: continue
            seen.add((x, y))
            comp.append((x, y))
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x+dx, y+dy
                if xmin <= nx <= xmax and ymin <= ny <= ymax:
                    q.append((nx, ny))
        return comp

    if len(uniform_cols) >= 2:
        c0, c1 = sorted(uniform_cols)[:2]
        border = grid[0][c0]
        bg = grid[0][c0+1]
        region_w = c1 - c0 - 1
        out = [[border] * (region_w + 2) for _ in range(h)]
        seen = set()
        comps = []
        for y in range(h):
            for x in range(c1+1, w):
                if (x, y) not in seen and grid[y][x] not in (bg, border):
                    col = grid[y][x]
                    comp = bfs(x, y, col, c1+1, w-1, 0, h-1, seen)
                    xs = [p[0] for p in comp]; ys = [p[1] for p in comp]
                    minx, maxx = min(xs), max(xs)
                    miny, maxy = min(ys), max(ys)
                    comps.append((miny, minx, maxy-miny+1, maxx-minx+1, comp))
        comps.sort(key=lambda t: (t[0], t[1]))
        cur_y = 0
        for miny, minx, hh, ww, comp in comps:
            off_x = (region_w - ww) // 2
            for x, y in comp:
                out[cur_y + (y - miny)][1 + off_x + (x - minx)] = grid[y][x]
            cur_y += hh
        return out
    else:
        r0, r1 = sorted(uniform_rows)[:2]
        border = grid[r0][0]
        bg = grid[r0+1][0]
        region_h = r1 - r0 - 1
        out = [[border] * w for _ in range(region_h + 2)]
        seen = set()
        comps = []
        for y in range(r0+1, r1):
            for x in range(w):
                if (x, y) not in seen and grid[y][x] not in (bg, border):
                    col = grid[y][x]
                    comp = bfs(x, y, col, 0, w-1, r0+1, r1-1, seen)
                    xs = [p[0] for p in comp]; ys = [p[1] for p in comp]
                    minx, maxx = min(xs), max(xs)
                    miny, maxy = min(ys), max(ys)
                    comps.append((minx, miny, maxx-minx+1, maxy-miny+1, comp))
        comps.sort(key=lambda t: (t[0], t[1]))
        cur_x = 0
        for minx, miny, ww, hh, comp in comps:
            off_y = (region_h - hh) // 2
            for x, y in comp:
                out[1 + off_y + (y - miny)][cur_x + (x - minx)] = grid[y][x]
            cur_x += ww
        return out