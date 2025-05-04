def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    shapes = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not vis[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                comp = []
                vis[i][j] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==col:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                rs = [x for x,y in comp]; cs = [y for x,y in comp]
                r0,r1,minc,maxc = min(rs), max(rs), min(cs), max(cs)
                bh, bw = r1-r0+1, maxc-minc+1
                if bh==bw and bh>=3:
                    ring = True
                    for x in range(r0, r1+1):
                        for y in range(minc, maxc+1):
                            if x in (r0,r1) or y in (minc,maxc):
                                if grid[x][y]!=col: ring=False
                            else:
                                if grid[x][y]!=0: ring=False
                    if ring:
                        shape = [row[minc:maxc+1] for row in grid[r0:r1+1]]
                        shapes.append((r0, minc, shape))
    shapes.sort(key=lambda x: x[0])
    n = len(shapes)
    if n==0: return []
    rs = []
    for r0,c0,sh in shapes: rs.append((r0, r0+len(sh)-1))
    overlap = any(not (r2<r3 or r4<r1) for i,(r1,r2) in enumerate(rs) for j,(r3,r4) in enumerate(rs) if i<j)
    sz = len(shapes[0][2])
    if overlap:
        H, W = sz, sz*n
        out = [[0]*W for _ in range(H)]
        for idx,(_,__,sh) in enumerate(shapes):
            for i in range(sz):
                for j in range(sz):
                    out[i][idx*sz+j] = sh[i][j]
    else:
        H, W = sz*n, sz
        out = [[0]*W for _ in range(H)]
        for idx,(_,__,sh) in enumerate(shapes):
            for i in range(sz):
                for j in range(sz):
                    out[idx*sz+i][j] = sh[i][j]
    return out