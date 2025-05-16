def solve(grid):
    h, w = len(grid), len(grid[0])
    axes = {}
    for c in range(w):
        col = [grid[r][c] for r in range(h)]
        prev = 0
        count = 0
        for x in col:
            if x and x == prev:
                count += 1
            else:
                count = 1
            prev = x
            if x and count > 1:
                axes[x] = (c, )
    color_axis = next(col for col in axes)
    cA = axes[color_axis][0]
    runs = []
    visited = [[False]*w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] and grid[r][c] != color_axis and not visited[r][c]:
                col = grid[r][c]
                stack = [(r,c)]
                comp = []
                visited[r][c] = True
                while stack:
                    y,x = stack.pop()
                    comp.append((y,x))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = y+dy, x+dx
                        if 0<=ny<h and 0<=nx<w and not visited[ny][nx] and grid[ny][nx]==col:
                            visited[ny][nx]=True
                            stack.append((ny,nx))
                runs.append((col, comp))
    out = [[0]*w for _ in range(h)]
    for r in range(h):
        out[r][cA] = color_axis
    r0 = min(r for r,_ in runs for r,_ in runs)
    top = sorted(runs, key=lambda x: min(pt[0] for pt in x[1]))
    for col, comp in top:
        anchor = min(comp, key=lambda p: abs(p[1]-cA))
        dr = -1 if min(p[0] for p in comp) < min(r for r,_ in runs) else -1
        dx = -1
        pts = sorted(comp, key=lambda p:(abs(p[0]-anchor[0])+abs(p[1]-anchor[1])))
        L = min(len(pts), abs(min(r for r,_ in runs)-anchor[0]))
        for i in range(L):
            ry = anchor[0] + dr*(i+1)
            cx = cA + dx*(i+1)
            if 0<=ry<h and 0<=cx<w:
                out[ry][cx] = col
    return out