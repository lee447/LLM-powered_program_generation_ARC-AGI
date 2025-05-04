def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] != 0 and not visited[y][x]:
                col = grid[y][x]
                stack = [(y, x)]
                pixels = []
                visited[y][x] = True
                while stack:
                    yy, xx = stack.pop()
                    pixels.append((yy, xx))
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = yy+dy, xx+dx
                        if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and grid[ny][nx] == col:
                            visited[ny][nx] = True
                            stack.append((ny, nx))
                ys = [p[0] for p in pixels]
                xs = [p[1] for p in pixels]
                ymin, ymax = min(ys), max(ys)
                xmin, xmax = min(xs), max(xs)
                ph, pw = ymax-ymin+1, xmax-xmin+1
                cnt = len(pixels)
                frame = cnt == 2*(ph+pw)-4
                comps.append({
                    'pixels': pixels,
                    'ymin': ymin, 'xmin': xmin,
                    'h': ph, 'w': pw,
                    'col': col, 'frame': frame
                })
    frames = [c for c in comps if c['frame']]
    nonf = [c for c in comps if not c['frame']]
    out = [[0]*w for _ in range(h)]
    frames.sort(key=lambda c: c['ymin'])
    placed = []
    for c in frames:
        y0 = 0
        while True:
            coll = False
            for yy, xx in c['pixels']:
                ny = y0 + (yy - c['ymin'])
                nx = xx
                if out[ny][nx] != 0:
                    coll = True
                    break
            if not coll:
                break
            y0 += c['h']
        for yy, xx in c['pixels']:
            out[y0 + (yy - c['ymin'])][xx] = c['col']
    nonf.sort(key=lambda c: c['xmin'])
    for c in nonf:
        y0 = h - c['h']
        for yy, xx in c['pixels']:
            out[y0 + (yy - c['ymin'])][xx] = c['col']
    return out