def solve(grid):
    h = len(grid)
    w = len(grid[0])
    visited = [[False]*w for _ in range(h)]
    holes = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==0 and not visited[i][j]:
                stack = [(i,j)]
                comp = []
                visited[i][j] = True
                touches = False
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    if x==0 or x==h-1 or y==0 or y==w-1:
                        touches = True
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==0:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                if not touches:
                    holes.append(comp)
    out = [row[:] for row in grid]
    for comp in holes:
        for i,j in comp:
            for di in (-1,0,1):
                for dj in (-1,0,1):
                    if di==0 and dj==0: continue
                    ni,nj = i+di, j+dj
                    if 0<=ni<h and 0<=nj<w:
                        out[ni][nj] = 7
    return out