def solve(grid):
    h, w = len(grid), len(grid[0])
    counts = {}
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v:
                counts[v] = counts.get(v, 0) + 1
    ps = sorted(counts, key=lambda x: -counts[x])[:2]
    p0, p1 = sorted(ps)
    comp = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def flood(i,j):
        stack = [(i,j)]
        comp[i][j] = True
        bb = [i,i,j,j]
        while stack:
            x,y = stack.pop()
            bb[0], bb[1] = min(bb[0],x), max(bb[1],x)
            bb[2], bb[3] = min(bb[2],y), max(bb[3],y)
            for dx,dy in dirs:
                nx,ny = x+dx, y+dy
                if 0<=nx<h and 0<=ny<w and not comp[nx][ny] and grid[nx][ny] in ps:
                    comp[nx][ny] = True
                    stack.append((nx,ny))
        return bb
    found = None
    for i in range(h):
        for j in range(w):
            if grid[i][j] in ps and not comp[i][j]:
                bb = flood(i,j)
                if found is None or (bb[1]-bb[0])*(bb[3]-bb[2]) > (found[1]-found[0])*(found[3]-found[2]):
                    found = bb
    r0, r1, c0, c1 = found
    P = [row[c0:c1+1] for row in grid[r0:r1+1]]
    ph, pw = r1-r0+1, c1-c0+1
    res = [row[:] for row in grid]
    quads = {
        'TR': (r0, c1+1, (r0, c1+pw), (r1, c1+1)),
        'BL': (r1+1, c0, (r1+1, c0+pw-1), (r1+ph, c0)),
        'BR': (r1+1, c1+1, (r1+1, c1+1), (r1+ph, c1+pw))
    }
    for q,(rs,cs,seed1,seed2) in quads.items():
        s1 = seed2 and 0<=seed2[0]<h and 0<=seed2[1]<w and grid[seed2[0]][seed2[1]] or grid[seed1[0]][seed1[1]] if seed1 and 0<=seed1[0]<h and 0<=seed1[1]<w else 0
        s2 = seed2 and 0<=seed2[0]<h and 0<=seed2[1]<w and grid[seed2[0]][seed2[1]] or 0
        a = grid[seed1[0]][seed1[1]] if seed1 and 0<=seed1[0]<h and 0<=seed1[1]<w else 0
        b = grid[seed2[0]][seed2[1]] if seed2 and 0<=seed2[0]<h and 0<=seed2[1]<w else 0
        if not (a or b): continue
        if a and b:
            m0 = s1 if p0>p1 else s2
            m1 = s2 if p0>p1 else s1
        else:
            m0 = m1 = a or b
        for i in range(ph):
            for j in range(pw):
                r, c = rs+i, cs+j
                if 0<=r<h and 0<=c<w:
                    res[r][c] = m0 if P[i][j]==p0 else m1
    return res