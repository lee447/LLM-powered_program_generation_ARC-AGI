def solve(grid):
    from collections import deque
    h, w = len(grid), len(grid[0])
    freq = {}
    for r in grid:
        for v in r:
            freq[v] = freq.get(v, 0) + 1
    bg = max(freq, key=freq.get)
    visited = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != bg and not visited[i][j]:
                col = grid[i][j]
                q = deque([(i,j)])
                visited[i][j] = True
                cells = []
                while q:
                    x,y = q.popleft()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==col:
                            visited[nx][ny] = True
                            q.append((nx,ny))
                rs = [x for x,y in cells]
                cs = [y for x,y in cells]
                rmin,rmax,minc,maxc = min(rs),max(rs),min(cs),max(cs)
                clusters.append({'rmin':rmin,'rmax':rmax,'cmin':minc,'cmax':maxc,'col':col,'cells':cells})
    clusters.sort(key=lambda c: ( (c['cmin']+c['cmax'])/2 ))
    groups = []
    for c in clusters:
        cc = (c['cmin']+c['cmax'])/2
        if not groups or abs(cc - groups[-1][0]['cmin'] - groups[-1][0]['cmax'])/2 > max(1,(w/10)):
            groups.append([c])
        else:
            groups[-1].append(c)
    for g in groups:
        g.sort(key=lambda c: (c['rmin']+c['rmax'])/2)
    out = [row[:] for row in grid]
    for g in groups:
        n = len(g)
        if n<2: continue
        for idx,c in enumerate(g):
            src = g[(idx+1)%n]
            for x,y in c['cells']:
                out[x][y] = src['col']
    return out