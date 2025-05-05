def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 3 and not visited[i][j]:
                comp = []
                stack = [(i,j)]
                visited[i][j] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == 3:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                clusters.append(comp)
    infos = []
    for comp in clusters:
        rs = [r for r,c in comp]
        cs = [c for r,c in comp]
        infos.append((min(cs), min(rs), max(rs), max(cs), comp))
    infos.sort(key=lambda x: x[0])
    empty = infos[0]
    a, b = infos[1], infos[2]
    blue, light = (a,8,1) if a[1] > b[1] else (b,8,1)
    if blue[1] > b[1]:
        blue = (b,1)
        light = (a,8)
    else:
        blue = (a,1)
        light = (b,8)
    for cluster,color in ((blue[0], blue[1]), (light[0], light[1])):
        _, r0, r1, c1, _ = cluster
        c0 = cluster[0]
        for i in range(r0+1, r1):
            for j in range(cluster[0]+1, c1):
                grid[i][j] = color
    return grid