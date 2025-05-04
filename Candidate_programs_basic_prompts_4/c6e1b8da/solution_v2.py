def solve(grid):
    H, W = len(grid), len(grid[0])
    seen = [[False]*W for _ in grid]
    comps = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0 and not seen[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                seen[i][j] = True
                cells = []
                while stack:
                    r,c = stack.pop()
                    cells.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and not seen[nr][nc] and grid[nr][nc]==col:
                            seen[nr][nc] = True
                            stack.append((nr,nc))
                comps.append((col, cells))
    pieces = []
    for col, cells in comps:
        s = set(cells)
        nbrs = {}
        for r,c in cells:
            cnt = 0
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                if (r+dr, c+dc) in s:
                    nbrs[(r,c)] = nbrs.get((r,c),0) + 1
                    cnt += 1
            if cnt:
                nbrs[(r,c)] = cnt
        corner = next(p for p,n in nbrs.items() if n==2)
        drs = []
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            if (corner[0]+dr, corner[1]+dc) in s:
                drs.append((dr,dc))
        vdir = drs[0][0] if drs[0][0]!=0 else drs[1][0]
        hdir = drs[0][1] if drs[0][1]!=0 else drs[1][1]
        offs = [(r-corner[0], c-corner[1]) for r,c in cells]
        # compute extents
        hext = max((c for r,c in offs)) if hdir>0 else -min((c for r,c in offs))
        vext = max((r for r,c in offs)) if vdir>0 else -min((r for r,c in offs))
        pieces.append({'col':col,'corner':corner,'offs':offs,'orient':(vdir,hdir),'hext':hext,'vext':vext})
    # sequence of orientations for spiral
    seq = [(1,1),(1,-1),(-1,-1),(-1,1),(1,1)]
    placed = []
    used = set()
    # for the first (1,1), pick the one with smallest corner[0]
    for idx, orient in enumerate(seq):
        candidates = [p for p in pieces if p['orient']==orient and p['col'] not in used]
        if len(candidates)>1:
            if idx==0:
                p = min(candidates, key=lambda p:p['corner'][0])
            else:
                p = candidates[0]
        else:
            p = candidates[0]
        placed.append(p)
        used.add(p['col'])
    # prepare output
    out = [[0]*W for _ in grid]
    # global nonzero bounds
    rr = [r for r in range(H) for c in range(W) if grid[r][c]!=0]
    cc = [c for r in range(H) for c in range(W) if grid[r][c]!=0]
    rmin, rmax = min(rr), max(rr)
    cmin, cmax = min(cc), max(cc)
    # place first at its original
    p1 = placed[0]
    base_r, base_c = p1['corner']
    for dr,dc in p1['offs']:
        out[base_r+dr][base_c+dc] = p1['col']
    # second: top-right pocket
    p2 = placed[1]
    nr = rmin
    nc = cmax - p2['hext']
    for dr,dc in p2['offs']:
        out[nr+dr][nc+dc] = p2['col']
    # third: bottom-right
    p3 = placed[2]
    nr = rmax - p3['vext']
    nc = cmax - p3['hext']
    for dr,dc in p3['offs']:
        out[nr+dr][nc+dc] = p3['col']
    # fourth: bottom-left
    p4 = placed[3]
    nr = rmax - p4['vext']
    nc = cmin
    for dr,dc in p4['offs']:
        out[nr+dr][nc+dc] = p4['col']
    # fifth: inner top-left
    p5 = placed[4]
    nr = rmin + p1['vext']
    nc = cmin + p1['hext']
    for dr,dc in p5['offs']:
        out[nr+dr][nc+dc] = p5['col']
    return out