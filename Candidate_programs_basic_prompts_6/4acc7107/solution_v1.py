def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import deque
    colors = set()
    for y in range(h):
        for x in range(w):
            if grid[y][x] != 0:
                colors.add(grid[y][x])
    comps_by_color = {}
    minx_by_color = {}
    for c in colors:
        visited = [[False]*w for _ in range(h)]
        comps = []
        minx = w
        for y in range(h):
            for x in range(w):
                if grid[y][x] == c:
                    minx = min(minx, x)
        minx_by_color[c] = minx
        for y in range(h):
            for x in range(w):
                if grid[y][x] == c and not visited[y][x]:
                    q = deque([(y, x)])
                    visited[y][x] = True
                    cells = []
                    while q:
                        yy, xx = q.popleft()
                        cells.append((yy, xx))
                        for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                            ny, nx = yy+dy, xx+dx
                            if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and grid[ny][nx] == c:
                                visited[ny][nx] = True
                                q.append((ny, nx))
                    ys = [p[0] for p in cells]
                    xs = [p[1] for p in cells]
                    y0, y1 = min(ys), max(ys)
                    x0, x1 = min(xs), max(xs)
                    comp = {
                        'color': c,
                        'size': len(cells),
                        'y0': y0, 'x0': x0,
                        'h': y1-y0+1, 'w': x1-x0+1,
                        'cells': [(yy-y0, xx-x0) for yy, xx in cells]
                    }
                    comps.append(comp)
        comps_by_color[c] = comps
    color_order = sorted(colors, key=lambda c: minx_by_color[c])
    region_w = {}
    for c in color_order:
        region_w[c] = max(comp['w'] for comp in comps_by_color[c])
    start_x = {}
    curx = 0
    for i, c in enumerate(color_order):
        start_x[c] = curx
        curx += region_w[c] + 1
    out = [[0]*w for _ in range(h)]
    for c in color_order:
        comps = sorted(comps_by_color[c], key=lambda comp: comp['size'])
        prev_y = h
        for comp in reversed(comps):
            y0 = prev_y - comp['h']
            x0 = start_x[c]
            for dy, dx in comp['cells']:
                out[y0+dy][x0+dx] = c
            prev_y = y0 - 1
    return out