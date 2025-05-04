def solve(grid):
    h = len(grid)
    w = len(grid[0])
    res = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                cc = []
                while stack:
                    y, x = stack.pop()
                    cc.append((y, x))
                    for dy, dx in dirs:
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and grid[ny][nx] == 1:
                            visited[ny][nx] = True
                            stack.append((ny, nx))
                ys = [y for y, x in cc]
                xs = [x for y, x in cc]
                minY, maxY = min(ys), max(ys)
                minX, maxX = min(xs), max(xs)
                if maxY-minY < 2 or maxX-minX < 2:
                    continue
                markers = []
                for yy in range(minY+1, maxY):
                    for xx in range(minX+1, maxX):
                        v = grid[yy][xx]
                        if v != 0 and v != 1:
                            markers.append((yy, xx, v))
                if not markers:
                    continue
                sy, sx, color = markers[0]
                fvis = [[False]*w for _ in range(h)]
                queue = [(sy, sx)]
                fvis[sy][sx] = True
                while queue:
                    y, x = queue.pop()
                    res[y][x] = color
                    for dy, dx in dirs:
                        ny, nx = y+dy, x+dx
                        if minY < ny < maxY and minX < nx < maxX and not fvis[ny][nx] and res[ny][nx] != 1:
                            fvis[ny][nx] = True
                            queue.append((ny, nx))
    return res