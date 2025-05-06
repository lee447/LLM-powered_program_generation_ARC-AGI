def solve(grid):
    from collections import deque
    H, W = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    # find reference shape of 2
    vis = [[False]*W for _ in range(H)]
    ref_cells = []
    for i in range(H):
        for j in range(W):
            if grid[i][j]==2 and not vis[i][j]:
                q = [(i,j)]
                vis[i][j]=True
                for x,y in q:
                    ref_cells.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and not vis[nx][ny] and grid[nx][ny]==2:
                            vis[nx][ny]=True
                            q.append((nx,ny))
                break
        if ref_cells: break
    rs = [r for r,c in ref_cells]; cs = [c for r,c in ref_cells]
    r0,c0 = min(rs), min(cs)
    h = max(rs)-r0+1; w = max(cs)-c0+1
    ref = [[0]*w for _ in range(h)]
    for r,c in ref_cells:
        ref[r-r0][c-c0] = 1
    # build all transforms of ref
    def rotate(m):
        Hm,Wm = len(m), len(m[0])
        return [[m[Hm-1-c][r] for c in range(Hm)] for r in range(Wm)]
    def flip(m):
        return [row[::-1] for row in m]
    mats = []
    m0 = ref
    for _ in range(4):
        mats.append(m0)
        mats.append(flip(m0))
        m0 = rotate(m0)
    mats = [m for i,m in enumerate(mats) if i%2==0]  # unique rotations and flips
    # find all 1-clusters
    comp = [[-1]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            if grid[i][j]==1 and comp[i][j]<0:
                cid = len(comps); comps.append([])
                q = deque([(i,j)]); comp[i][j]=cid
                while q:
                    x,y = q.popleft(); comps[cid].append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and grid[nx][ny]==1 and comp[nx][ny]<0:
                            comp[nx][ny]=cid; q.append((nx,ny))
    # for each comp test if it contains a transform of ref
    to_color = [False]*len(comps)
    for cid,cells in enumerate(comps):
        rs = [r for r,c in cells]; cs = [c for r,c in cells]
        R0,C0 = min(rs), min(cs)
        Rh = max(rs)-R0+1; Cw = max(cs)-C0+1
        # build mask of comp
        mask = [[0]*Cw for _ in range(Rh)]
        for r,c in cells:
            mask[r-R0][c-C0] = 1
        # try to embed any transform
        for t in mats:
            th, tw = len(t), len(t[0])
            if th>Rh or tw>Cw: continue
            for i0 in range(Rh-th+1):
                for j0 in range(Cw-tw+1):
                    ok = True
                    for ii in range(th):
                        for jj in range(tw):
                            if t[ii][jj]==1 and mask[i0+ii][j0+jj]!=1:
                                ok=False; break
                        if not ok: break
                    if ok:
                        to_color[cid]=True; break
                if to_color[cid]: break
            if to_color[cid]: break
    # build output
    out = [row[:] for row in grid]
    for cid,flag in enumerate(to_color):
        if flag:
            for r,c in comps[cid]:
                out[r][c] = 2
    return out