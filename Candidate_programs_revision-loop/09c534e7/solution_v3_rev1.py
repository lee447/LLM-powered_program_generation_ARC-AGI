def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    out = [row[:] for row in grid]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                markers = set()
                while stack:
                    x, y = stack.pop()
                    comp.append((x,y))
                    if grid[x][y] > 1:
                        markers.add(grid[x][y])
                    for dx, dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != 0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                if markers:
                    c = next(iter(markers))
                    for x, y in comp:
                        interior = True
                        for dx, dy in dirs:
                            nx, ny = x+dx, y+dy
                            if nx < 0 or nx >= h or ny < 0 or ny >= w or grid[nx][ny] == 0:
                                interior = False
                                break
                        if interior:
                            out[x][y] = c
                    for x, y in comp:
                        if grid[x][y] > 1:
                            out[x][y] = c
    return out