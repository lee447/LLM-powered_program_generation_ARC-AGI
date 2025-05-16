def solve(grid):
    h = len(grid)
    w = len(grid[0])
    background = grid[0][0]
    shapeColor = 1 - background
    out = [row[:] for row in grid]
    if background == 0:
        visited_s = [[False]*w for _ in range(h)]
        largest = []
        for i in range(h):
            for j in range(w):
                if grid[i][j] == shapeColor and not visited_s[i][j]:
                    stack = [(i,j)]
                    visited_s[i][j] = True
                    comp = []
                    while stack:
                        x,y = stack.pop()
                        comp.append((x,y))
                        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                            nx,ny = x+dx, y+dy
                            if 0<=nx<h and 0<=ny<w and not visited_s[nx][ny] and grid[nx][ny]==shapeColor:
                                visited_s[nx][ny] = True
                                stack.append((nx,ny))
                    if len(comp) > len(largest):
                        largest = comp
        shapeSet = set(largest)
        for i in range(h):
            for j in range(w):
                if grid[i][j] == shapeColor and (i,j) not in shapeSet:
                    out[i][j] = background
    visited_h = [[False]*w for _ in range(h)]
    holes = []
    for i in range(h):
        for j in range(w):
            if out[i][j] == background and not visited_h[i][j]:
                stack = [(i,j)]
                visited_h[i][j] = True
                comp = []
                touches = False
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    if x==0 or x==h-1 or y==0 or y==w-1:
                        touches = True
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not visited_h[nx][ny] and out[nx][ny]==background:
                            visited_h[nx][ny] = True
                            stack.append((nx,ny))
                if not touches:
                    holes.append(comp)
    for comp in holes:
        for i,j in comp:
            for di in (-1,0,1):
                for dj in (-1,0,1):
                    if di==0 and dj==0: continue
                    ni,nj = i+di, j+dj
                    if 0<=ni<h and 0<=nj<w:
                        out[ni][nj] = 7
    return out