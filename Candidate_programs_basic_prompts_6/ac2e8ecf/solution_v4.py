def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import defaultdict, deque
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c!=0 and not vis[i][j]:
                q = deque([(i,j)])
                vis[i][j] = True
                cells = []
                while q:
                    x,y = q.popleft()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==c:
                            vis[nx][ny] = True
                            q.append((nx,ny))
                rs = [x for x,_ in cells]
                cs = [y for _,y in cells]
                comps.append((c, min(rs), max(rs), min(cs), max(cs), cells))
    cnt = defaultdict(int)
    for c,_,_,_,_,_ in comps:
        cnt[c]+=1
    pivot = max(cnt, key=lambda c:cnt[c])
    pivots = [c for c in comps if c[0]==pivot]
    pivots.sort(key=lambda x:x[1])
    others = [c for c in comps if c[0]!=pivot]
    others.sort(key=lambda x:x[1])
    out = [[0]*w for _ in range(h)]
    # pair pivot parts with others
    pairs = min(len(pivots), len(others))
    top_h = pivots[0][2]-pivots[0][1]+1
    for i in range(pairs):
        pc, pr0, pr1, pc0, pc1, pcells = pivots[i]
        oc, or0, or1, oc0, oc1, ocells = others[i]
        if i==0:
            rshift_p = -pr0
            rshift_o = -or0
        else:
            rshift_p = h-(pr1+1)
            rshift_o = h-(or1+1)
        for x,y in pcells:
            out[x+rshift_p][y] = pc
        for x,y in ocells:
            out[x+rshift_o][y] = oc
    # leftover others
    rem = others[pairs:]
    if rem:
        base = top_h
        for oc, or0, or1, oc0, oc1, ocells in rem:
            rshift = base - or0
            for x,y in ocells:
                out[x+rshift][y] = oc
    return out