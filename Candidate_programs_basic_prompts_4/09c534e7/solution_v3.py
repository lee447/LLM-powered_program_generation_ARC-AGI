def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] > 1 and not visited[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                comp = []
                visited[i][j] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                            if grid[nx][ny] == 1 or grid[nx][ny] == col:
                                visited[nx][ny] = True
                                stack.append((nx,ny))
                comp_set = set(comp)
                for x,y in comp:
                    interior = True
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if (nx,ny) not in comp_set:
                            interior = False
                            break
                    if interior:
                        out[x][y] = col
    return out