def solve(grid):
    h = len(grid)
    w = len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
                        nx,ny = x+dx,y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] != 0:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                comps.append(comp)
    if not comps:
        return []
    comp = max(comps, key=len)
    rs = [r for r,c in comp]
    cs = [c for r,c in comp]
    r0,r1 = min(rs),max(rs)
    c0,c1 = min(cs),max(cs)
    sub = [row[c0:c1+1] for row in grid[r0:r1+1]]
    H = len(sub)
    W = len(sub[0])
    if H > W:
        d = H - W
        l = d//2
        r = d - l
        sub = [([0]*l + row + [0]*r) for row in sub]
    elif W > H:
        d = W - H
        t = d//2
        b = d - t
        pad = [[0]*W for _ in range(t)]
        sub = pad + sub + [[0]*W for _ in range(b)]
    return sub