def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    vis = [[False]*w for _ in range(h)]
    rects = []
    others = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] != 0 and not vis[y][x]:
                col = grid[y][x]
                stack = [(y,x)]
                vis[y][x] = True
                cells = []
                while stack:
                    cy, cx = stack.pop()
                    cells.append((cy,cx))
                    for dy, dx in dirs:
                        ny, nx = cy+dy, cx+dx
                        if 0 <= ny < h and 0 <= nx < w and not vis[ny][nx] and grid[ny][nx] == col:
                            vis[ny][nx] = True
                            stack.append((ny,nx))
                ys = [cy for cy, cx in cells]
                xs = [cx for cy, cx in cells]
                y0, y1 = min(ys), max(ys)
                x0, x1 = min(xs), max(xs)
                hh, ww = y1-y0+1, x1-x0+1
                cnt = len(cells)
                if cnt == hh*ww or cnt == 2*(hh+ww)-4:
                    rects.append((cells, col, y0))
                else:
                    others.append((cells, col, y0))
    out = [[0]*w for _ in range(h)]
    for cells, col, y0 in rects:
        for cy, cx in cells:
            out[cy-y0][cx] = col
    if others and rects:
        mh = max((max(cy for cy, cx in cells) - min(cy for cy, cx in cells) + 1) for cells, col, y0 in rects)
        base = h - mh
        for cells, col, y0 in others:
            for cy, cx in cells:
                out[base + (cy-y0)][cx] = col
    return out