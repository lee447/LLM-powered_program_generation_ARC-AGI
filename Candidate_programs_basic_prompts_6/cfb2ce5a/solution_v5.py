def solve(grid):
    H, W = len(grid), len(grid[0])
    vis = [[False]*W for _ in range(H)]
    # find cluster region
    from collections import deque
    found = False
    for si in range(H):
        for sj in range(W):
            if grid[si][sj] != 0:
                dq = deque([(si, sj)])
                vis[si][sj] = True
                region = []
                while dq:
                    i, j = dq.popleft()
                    region.append((i, j))
                    for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                        ni, nj = i+di, j+dj
                        if 0 <= ni < H and 0 <= nj < W and not vis[ni][nj] and grid[ni][nj] != 0:
                            vis[ni][nj] = True
                            dq.append((ni, nj))
                found = True
                break
        if found: break
    rs = [i for i,j in region]
    cs = [j for i,j in region]
    r0, r1 = min(rs), max(rs)
    c0, c1 = min(cs), max(cs)
    h, w = r1-r0+1, c1-c0+1
    P = [row[c0:c1+1] for row in grid[r0:r0+1+h-1][0:1]]  # dummy, will fix
    P = [grid[i][c0:c1+1] for i in range(r0, r1+1)]
    # pattern symbols
    pv1 = grid[r0][c0]
    syms = set()
    for row in P:
        for v in row:
            syms.add(v)
    syms = list(sorted(syms))
    if len(syms) == 2:
        s1, s2 = syms[0], syms[1]
    else:
        s1, s2 = pv1, next(v for v in syms if v != pv1)
    # rotations
    def rot_cw(M):
        return [[M[h-1-j][i] for j in range(h)] for i in range(w)]
    def rot_ccw(M):
        return [[M[j][w-1-i] for j in range(h)] for i in range(w)]
    def rot_180(M):
        return [[M[h-1-i][w-1-j] for j in range(w)] for i in range(h)]
    out = [row[:] for row in grid]
    # block origins
    blocks = [ (r0, c0), (r0, c0+w), (r0+h, c0), (r0+h, c0+w) ]
    for bi, bj in blocks:
        if bi == r0 and bj == c0: continue
        # gather border seeds
        top = [grid[bi][bj+j] for j in range(w)]
        left = [grid[bi+i][bj] for i in range(h)]
        topp = [v for v in top if v!=0]
        leftp = [v for v in left if v!=0]
        seeds = set(topp+leftp)
        if not seeds: continue
        # decide rotation and mapping
        if bi==r0 and bj>c0:  # top-right
            M = rot_cw(P)
            # mapping: s1->seed_left if len(leftp)==1 else s1->leftp[0], s2->seed_top
            st = topp[0] if topp else 0
            sl = leftp[0] if leftp else 0
            # choose mapping by example1 style
            if sl < st:
                m1, m2 = sl, st
            else:
                m1, m2 = st, sl
        elif bi>r0 and bj==c0:  # bottom-left
            M = rot_ccw(P)
            st = topp[0] if topp else 0
            sl = leftp[0] if leftp else 0
            if sl < st:
                m1, m2 = st, sl
            else:
                m1, m2 = sl, st
        else:  # bottom-right
            M = rot_180(P)
            st = topp[0] if topp else 0
            sl = leftp[0] if leftp else 0
            # one seed only
            m1, m2 = 0, st or sl
        # fill
        for i in range(len(M)):
            for j in range(len(M[0])):
                v = M[i][j]
                if v == s1 and m1:
                    out[bi+i][bj+j] = m1
                elif v == s2 and m2:
                    out[bi+i][bj+j] = m2
    return out
def solve(grid):
    H, W = len(grid), len(grid[0])
    # find cluster by BFS of non-zero region
    from collections import deque
    vis = [[False]*W for _ in range(H)]
    cluster = []
    for si in range(H):
        for sj in range(W):
            if grid[si][sj] != 0:
                dq = deque([(si,sj)])
                vis[si][sj] = True
                while dq:
                    i,j = dq.popleft()
                    cluster.append((i,j))
                    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                        ni,nj = i+di, j+dj
                        if 0<=ni<H and 0<=nj<W and not vis[ni][nj] and grid[ni][nj]!=0:
                            vis[ni][nj] = True
                            dq.append((ni,nj))
                si = H
                break
        else:
            continue
        break
    rs = [i for i,j in cluster]
    cs = [j for i,j in cluster]
    r0,r1 = min(rs), max(rs)
    c0,c1 = min(cs), max(cs)
    h, w = r1-r0+1, c1-c0+1
    P = [grid[i][c0:c1+1] for i in range(r0, r1+1)]
    vals = sorted({v for row in P for v in row})
    if len(vals)==2:
        s1,s2 = vals
    else:
        s1 = grid[r0][c0]
        s2 = next(v for v in vals if v!=s1)
    def rot_cw(M):
        return [[M[h-1-j][i] for j in range(h)] for i in range(w)]
    def rot_ccw(M):
        return [[M[j][w-1-i] for j in range(h)] for i in range(w)]
    def rot_180(M):
        return [[M[h-1-i][w-1-j] for j in range(w)] for i in range(h)]
    out = [row[:] for row in grid]
    # block origins (top-left, top-right, bottom-left, bottom-right)
    blocks = [(r0,c0),(r0,c0+w),(r0+h,c0),(r0+h,c0+w)]
    for bi,bj in blocks:
        if bi==r0 and bj==c0: continue
        # collect seeds on top edge and left edge of this block
        top = [grid[bi][bj+j] for j in range(w)]
        left = [grid[bi+i][bj] for i in range(h)]
        tvals = [v for v in top if v!=0]
        lvals = [v for v in left if v!=0]
        if not tvals and not lvals: continue
        # decide rotation and mapping
        if bi==r0 and bj>c0:  # top-right
            M = rot_cw(P)
            seed_t = tvals[0] if tvals else 0
            seed_l = lvals[0] if lvals else 0
            # example-based choice
            m1,m2 = (seed_l,seed_t) if seed_l<seed_t else (seed_t,seed_l)
        elif bi>r0 and bj==c0:  # bottom-left
            M = rot_ccw(P)
            seed_t = tvals[0] if tvals else 0
            seed_l = lvals[0] if lvals else 0
            m1,m2 = (seed_t,seed_l) if seed_l<seed_t else (seed_l,seed_t)
        else:  # bottom-right
            M = rot_180(P)
            seed_t = tvals[0] if tvals else 0
            seed_l = lvals[0] if lvals else 0
            m1,m2 = 0, seed_t or seed_l
        sh, sw = len(M), len(M[0])
        for i in range(sh):
            for j in range(sw):
                v = M[i][j]
                if v==s1 and m1:
                    out[bi+i][bj+j] = m1
                elif v==s2 and m2:
                    out[bi+i][bj+j] = m2
    return out