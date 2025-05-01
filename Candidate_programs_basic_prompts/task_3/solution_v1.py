def solve(grid):
    m, n = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    visited = [[False]*n for _ in range(m)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    eight = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0 and not visited[i][j]:
                comp = []
                stack = [(i,j)]
                visited[i][j] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] != 0:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                seed = None
                for x,y in comp:
                    if grid[x][y] > 1:
                        seed = grid[x][y]
                        break
                if seed is None:
                    continue
                comp_set = set(comp)
                for x,y in comp:
                    ok = True
                    for dx,dy in eight:
                        if (x+dx, y+dy) not in comp_set:
                            ok = False
                            break
                    if ok:
                        out[x][y] = seed
    return out