def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==5 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==5:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                comps.append(comp)
    count = 0
    for comp in comps:
        cols = {y for _,y in comp}
        if len(comp)==4 and len(cols)>1:
            count += 1
        elif len(comp)>=2 and len(cols)==1:
            count += 1
    return [[0] for _ in range(count)]