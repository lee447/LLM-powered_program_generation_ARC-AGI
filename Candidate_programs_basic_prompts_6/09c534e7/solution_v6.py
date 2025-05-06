def solve(grid):
    h = len(grid)
    w = len(grid[0])
    outside = [[False]*w for _ in range(h)]
    q = []
    for i in range(h):
        for j in (0, w-1):
            if grid[i][j] != 1 and not outside[i][j]:
                outside[i][j] = True
                q.append((i, j))
    for j in range(w):
        for i in (0, h-1):
            if grid[i][j] != 1 and not outside[i][j]:
                outside[i][j] = True
                q.append((i, j))
    while q:
        i, j = q.pop(0)
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = i+di, j+dj
            if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] != 1 and not outside[ni][nj]:
                outside[ni][nj] = True
                q.append((ni, nj))
    vis = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 1 and not outside[i][j] and not vis[i][j]:
                region = []
                q = [(i, j)]
                vis[i][j] = True
                while q:
                    x, y = q.pop(0)
                    region.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != 1 and not outside[nx][ny] and not vis[nx][ny]:
                            vis[nx][ny] = True
                            q.append((nx, ny))
                colors = {grid[x][y] for x, y in region if grid[x][y] != 0}
                if len(colors) == 1:
                    c = colors.pop()
                    for x, y in region:
                        if grid[x][y] == 0:
                            grid[x][y] = c
    return grid