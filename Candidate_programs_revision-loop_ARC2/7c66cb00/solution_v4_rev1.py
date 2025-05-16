import numpy as np

def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    blank = [all(c == bg for c in row) for row in grid]
    stripes = []
    i = 0
    while i < h:
        if blank[i]:
            i += 1
            continue
        j = i
        while j < h and not blank[j]:
            j += 1
        stripes.append((i, j))
        i = j
    y0, y1 = stripes[0]
    visited = [[False]*w for _ in range(h)]
    shapes = []
    for y in range(y0, y1):
        for x in range(w):
            if not visited[y][x] and grid[y][x] != bg:
                col0 = grid[y][x]
                stack = [(y, x)]
                comp = []
                visited[y][x] = True
                while stack:
                    yy, xx = stack.pop()
                    comp.append((yy, xx))
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = yy+dy, xx+dx
                        if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and grid[ny][nx] != bg:
                            visited[ny][nx] = True
                            stack.append((ny, nx))
                if len(comp) > 1:
                    ys = [p[0] for p in comp]; xs = [p[1] for p in comp]
                    sy0, sy1 = min(ys), max(ys)
                    sx0, sx1 = min(xs), max(xs)
                    pixels = [(yy-sy0, xx-sx0, grid[yy][xx]) for yy, xx in comp]
                    shapes.append((sy1-sy0+1, sx1-sx0+1, sy0, sx0, pixels))
    shapes.sort(key=lambda s: s[0]*s[1], reverse=True)
    out = [row[:] for row in grid]
    for idx, (sy0, sy1) in enumerate(stripes[1:], 1):
        sh_index = (idx-1) % len(shapes)
        sh_h, sh_w, oy0, ox0, pixels = shapes[sh_index]
        cols = [x for x in range(w) if any(grid[y][x] != bg for y in range(sy0, sy1))]
        if not cols: continue
        cx0, cx1 = min(cols), max(cols)
        interior_counts = {}
        for y in range(sy0+1, sy1-1):
            for x in range(cx0+1, cx1):
                c = grid[y][x]
                if c != bg:
                    interior_counts[c] = interior_counts.get(c, 0) + 1
        sc_int = max(interior_counts, key=interior_counts.get) if interior_counts else bg
        border_counts = {}
        for x in range(cx0, cx1+1):
            for y in (sy0, sy1-1):
                c = grid[y][x]
                if c != bg:
                    border_counts[c] = border_counts.get(c, 0) + 1
        for y in range(sy0, sy1):
            for x in (cx0, cx1):
                c = grid[y][x]
                if c != bg:
                    border_counts[c] = border_counts.get(c, 0) + 1
        sc_bor = max(border_counts, key=border_counts.get) if border_counts else bg
        cols_sh = set(c for _, _, c in pixels)
        if len(cols_sh) == 1:
            bor = None
        else:
            cnts = {c: 0 for c in cols_sh}
            for _, _, c in pixels: cnts[c] += 1
            a, b = cols_sh
            bor = a if cnts[a] > cnts[b] else b
        stripe_h = sy1 - sy0
        stripe_w = cx1 - cx0 + 1
        ty = sy0 + (stripe_h - sh_h)//2
        tx = cx0 + (stripe_w - sh_w)//2
        for dy, dx, c in pixels:
            y, x = ty+dy, tx+dx
            if 0 <= y < h and 0 <= x < w:
                if bor is None:
                    out[y][x] = sc_int
                else:
                    out[y][x] = sc_bor if c == bor else sc_int
    return out