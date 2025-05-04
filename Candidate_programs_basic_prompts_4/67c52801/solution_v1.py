def solve(grid):
    from collections import deque
    R, C = len(grid), len(grid[0])
    # find mask color
    last = grid[-1]
    freq = {}
    for v in last:
        if v != 0:
            freq[v] = freq.get(v, 0) + 1
    mask_color = max(freq, key=lambda k: freq[k])
    # mask positions
    mask_pos = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == mask_color]
    r_min = min(r for r, _ in mask_pos); r_max = max(r for r, _ in mask_pos)
    c_min = min(c for _, c in mask_pos); c_max = max(c for _, c in mask_pos)
    mask_height = r_max - r_min + 1
    # find shapes
    seen = [[False]*C for _ in range(R)]
    shapes = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] != 0 and grid[i][j] != mask_color and not seen[i][j]:
                col = grid[i][j]
                q = deque([(i,j)])
                seen[i][j] = True
                cells = []
                while q:
                    x,y = q.popleft()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0<=nx<R and 0<=ny<C and not seen[nx][ny] and grid[nx][ny]==col:
                            seen[nx][ny] = True
                            q.append((nx, ny))
                rs = [x for x,_ in cells]; cs = [y for _,y in cells]
                r0, r1 = min(rs), max(rs); c0, c1 = min(cs), max(cs)
                h, w = r1-r0+1, c1-c0+1
                mat = [[0]*w for _ in range(h)]
                for x,y in cells:
                    mat[x-r0][y-c0] = col
                shapes.append({'color':col,'mat':mat,'h':h,'w':w})
    # find segments
    segs = []
    c = c_min
    while c <= c_max:
        if grid[r_min][c] != mask_color:
            start = c
            while c<=c_max and grid[r_min][c] != mask_color:
                c+=1
            segs.append((start, c-1))
        else:
            c+=1
    # rotation
    def rotate(mat, h, w):
        m2 = [[0]*h for _ in range(w)]
        for i in range(w):
            for j in range(h):
                m2[i][j] = mat[h-1-j][i]
        return m2, w, h
    # prepare variants
    variants = []
    for idx,sh in enumerate(shapes):
        mat, h, w = sh['mat'], sh['h'], sh['w']
        vs = []
        vs.append((mat, h, w))
        rm, rh, rw = rotate(mat, h, w)
        if not (rh==h and rw==w):
            vs.append((rm, rh, rw))
        variants.append(vs)
    S, M = len(shapes), len(segs)
    assign = [None]*M
    used = [False]*S
    def dfs(si):
        if si==M:
            return True
        seg_w = segs[si][1] - segs[si][0] + 1
        for i in range(S):
            if not used[i]:
                for mat,h,w in variants[i]:
                    if w==seg_w and h<=mask_height:
                        used[i] = True
                        assign[si] = (i, mat, h, w)
                        if dfs(si+1):
                            return True
                        used[i] = False
        return False
    dfs(0)
    # build output
    out = [[0]*C for _ in range(R)]
    for r,c in mask_pos:
        out[r][c] = mask_color
    for si,(start,end) in enumerate(segs):
        i, mat, h, w = assign[si]
        off_r = r_min - h
        for a in range(h):
            for b in range(w):
                if mat[a][b]!=0:
                    out[off_r + 1 + a][start + b] = mat[a][b]
    return out