def solve(grid):
    h, w = len(grid), len(grid[0])
    g = [row[:] for row in grid]
    seen = [[False]*w for _ in range(h)]
    rects = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==5 and not seen[i][j]:
                stack = [(i,j)]
                seen[i][j] = True
                cells = []
                while stack:
                    x,y = stack.pop()
                    cells.append((x,y))
                    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==5:
                            seen[nx][ny]=True
                            stack.append((nx,ny))
                xs = [x for x,y in cells]
                ys = [y for x,y in cells]
                minx,maxx = min(xs), max(xs)
                miny,maxy = min(ys), max(ys)
                rects.append((minx,maxx,miny,maxy))
    for minx,maxx,miny,maxy in rects:
        for x in range(minx, maxx+1):
            for y in range(miny, maxy+1):
                if grid[x][y]==0:
                    g[x][y] = 2
        bar_row = minx - 1
        length = maxy - miny + 1
        start = miny
        if 0<=bar_row<h:
            for y in range(start, start+length):
                if 0<=y<w:
                    g[bar_row][y] = 2
    return g