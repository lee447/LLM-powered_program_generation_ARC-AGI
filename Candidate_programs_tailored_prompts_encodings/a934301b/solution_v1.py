def solve(grid):
    H = len(grid)
    W = len(grid[0])
    visited = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            if not visited[i][j] and grid[i][j] != 0:
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] != 0:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                rows = [x for x,y in comp]
                cols = [y for x,y in comp]
                rmin, rmax = min(rows), max(rows)
                cmin, cmax = min(cols), max(cols)
                height = rmax - rmin + 1
                width = cmax - cmin + 1
                if len(comp) == height * width:
                    cnt8 = sum(1 for x,y in comp if grid[x][y] == 8)
                    if cnt8 == 1:
                        comps.append(comp)
    out = [[0]*W for _ in range(H)]
    for comp in comps:
        for x,y in comp:
            out[x][y] = grid[x][y]
    return out