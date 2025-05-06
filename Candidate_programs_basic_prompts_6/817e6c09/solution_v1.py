def solve(grid):
    import math
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 2 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == 2:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                comps.append(comp)
    centers = [(sum(x for x,y in c)/len(c), sum(y for x,y in c)/len(c)) for c in comps]
    cx = sum(x for x,y in centers)/len(centers)
    cy = sum(y for x,y in centers)/len(centers)
    angs = []
    for comp, (x,y) in zip(comps, centers):
        ang = math.atan2(x-cx, y-cy)
        angs.append((ang, comp))
    angs.sort(key=lambda x: x[0])
    sel = set()
    for idx, (_, comp) in enumerate(angs):
        if idx % 2 == 0:
            for p in comp:
                sel.add(p)
    out = [row[:] for row in grid]
    for i,j in sel:
        out[i][j] = 8
    return out