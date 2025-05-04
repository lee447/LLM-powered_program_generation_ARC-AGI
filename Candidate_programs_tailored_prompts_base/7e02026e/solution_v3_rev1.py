def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False] * w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 0 and not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                comp = []
                while stack:
                    x, y = stack.pop()
                    comp.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                comps.append(comp)
    sizes = [len(c) for c in comps]
    main = max(sizes) if sizes else 0
    out = [row[:] for row in grid]
    for comp in comps:
        s = len(comp)
        if s >= 5 and s < main:
            for x, y in comp:
                out[x][y] = 3
    return out