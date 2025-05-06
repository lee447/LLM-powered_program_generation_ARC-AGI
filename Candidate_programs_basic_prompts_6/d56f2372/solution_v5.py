def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                c = grid[i][j]
                stack = [(i,j)]
                visited[i][j] = True
                coords = []
                while stack:
                    x,y = stack.pop()
                    coords.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==c:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                comps.append((c,coords))
    def get_box(coords):
        rs = [r for r,_ in coords]; cs = [c for _,c in coords]
        r0,r1,minc,maxc = min(rs), max(rs), min(cs), max(cs)
        sub = [[0]*(maxc-minc+1) for _ in range(r1-r0+1)]
        for r,c in coords:
            sub[r-r0][c-minc] = grid[r][c]
        return sub
    syms = []
    for c,coords in comps:
        sub = get_box(coords)
        ok = True
        for row in sub:
            if row != row[::-1]:
                ok = False; break
        if ok:
            syms.append(sub)
    best = None
    for s in syms:
        if best is None or len(s)>len(best) or (len(s)==len(best) and len(s[0])>len(best[0])):
            best = s
    return best