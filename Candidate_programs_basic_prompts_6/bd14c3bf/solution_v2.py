def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    vis = [[False]*w for _ in range(h)]
    res = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not vis[i][j]:
                stack = [(i,j)]
                comp = []
                vis[i][j] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==1:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                xs = [x for x,y in comp]
                ys = [y for x,y in comp]
                minx, maxx = min(xs), max(xs)
                miny, maxy = min(ys), max(ys)
                bb_h = maxx-minx+1
                bb_w = maxy-miny+1
                area = len(comp)
                if area>=7 and not (bb_h<=3 and bb_w<=3):
                    for x,y in comp:
                        res[x][y] = 2
    return res