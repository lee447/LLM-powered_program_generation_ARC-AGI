def solve(grid):
    H, W = len(grid), len(grid[0])
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    vis = [[False]*W for _ in range(H)]
    clusters = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 3 and not vis[i][j]:
                stk = [(i,j)]
                vis[i][j] = True
                comp = []
                while stk:
                    r,c = stk.pop()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<H and 0<=nc<W and grid[nr][nc]==3 and not vis[nr][nc]:
                            vis[nr][nc] = True
                            stk.append((nr,nc))
                clusters.append(comp)
    bbs = []
    for comp in clusters:
        rs = [r for r,c in comp]
        cs = [c for r,c in comp]
        r0,r1,minc,maxc = min(rs), max(rs), min(cs), max(cs)
        bbs.append((r0,r1,minc,maxc))
    areas = [(r1-r0+1)*(maxc-minc+1) for (r0,r1,minc,maxc),(r1_,r2_,minc2,maxc2) in zip(bbs,bbs)]
    central_i = min(range(len(clusters)), key=lambda i: areas[i])
    cr0, cr1, cc0, cc1 = bbs[central_i]
    mid_r = (cr0+cr1)//2
    mid_c = (cc0+cc1)//2
    central_set = set(clusters[central_i])
    def sign(x): return (x>0) - (x<0)
    for idx, comp in enumerate(clusters):
        if idx == central_i: continue
        r0_, r1_, c0_, c1_ = bbs[idx]
        comp_set = set(comp)
        hole = None
        for r in range(r0_, r1_+1):
            for c in range(c0_, c1_+1):
                if grid[r][c] == 0:
                    h_nb = ((r-1,c) in comp_set) or ((r+1,c) in comp_set)
                    v_nb = ((r,c-1) in comp_set) or ((r,c+1) in comp_set)
                    if h_nb and v_nb:
                        hole = (r,c)
                        break
            if hole: break
        if not hole: continue
        hr, hc = hole
        dr = sign(mid_r - hr) if abs(mid_r - hr) >= abs(mid_c - hc) else 0
        dc = sign(mid_c - hc) if abs(mid_c - hc) > abs(mid_r - hr) else 0
        if dr == 0 and dc != 0:
            target_c = cc0+1 if dc>0 else cc1-1
            for c in range(hc+dc, target_c+dc, dc):
                grid[hr][c] = 3
        if dc == 0 and dr != 0:
            target_r = cr0+1 if dr>0 else cr1-1
            for r in range(hr+dr, target_r+dr, dr):
                grid[r][hc] = 3
    grid[cr0][mid_c] = 0
    grid[cr1][mid_c] = 0
    grid[mid_r][cc0] = 0
    grid[mid_r][cc1] = 0
    return grid