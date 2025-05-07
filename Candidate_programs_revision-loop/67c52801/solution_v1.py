def solve(grid):
    h, w = len(grid), len(grid[0])
    border = grid[-1][0]
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c != 0 and c != border and not visited[i][j]:
                cols = []
                stack = [(i,j)]
                visited[i][j] = True
                while stack:
                    x,y = stack.pop()
                    cols.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==c:
                            visited[nx][ny]=True
                            stack.append((nx,ny))
                comps.append((c, cols))
    blocks = []
    for col, pts in comps:
        rs = [p[0] for p in pts]; cs = [p[1] for p in pts]
        r0, r1 = min(rs), max(rs)
        c0, c1 = min(cs), max(cs)
        bh, bw = r1-r0+1, c1-c0+1
        mat = [[0]*bw for _ in range(bh)]
        for (x,y) in pts:
            mat[x-r0][y-c0] = col
        if bh != 2:
            nm = [[0]*bh for _ in range(bw)]
            for ii in range(bh):
                for jj in range(bw):
                    if mat[ii][jj]:
                        nm[jj][bh-1-ii] = col
            mat = nm
            bh, bw = len(mat), len(mat[0])
        blocks.append((len(pts), mat, col))
    blocks.sort(key=lambda x: x[0])
    newg = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if newg[i][j] != border:
                newg[i][j] = 0
    top = h-3; bot = h-2
    p = 0
    for _, mat, col in blocks:
        bh, bw = len(mat), len(mat[0])
        while True:
            if p + bw <= w:
                ok = True
                for i in range(bh):
                    for j in range(bw):
                        if mat[i][j] and newg[top + i][p + j] != 0:
                            ok = False; break
                    if not ok: break
                if ok: break
            p += 1
        for i in range(bh):
            for j in range(bw):
                if mat[i][j]:
                    newg[top + i][p + j] = col
        p += bw
    return newg