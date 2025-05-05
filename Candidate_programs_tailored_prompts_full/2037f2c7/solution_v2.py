def solve(grid):
    h, w = len(grid), len(grid[0])
    # collect nonzero coords
    seen = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not seen[i][j]:
                comp = []
                stack = [(i,j)]
                seen[i][j] = True
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and grid[nr][nc]!=0 and not seen[nr][nc]:
                            seen[nr][nc] = True
                            stack.append((nr,nc))
                clusters.append(comp)
    # pick the cluster with larger min col
    best = max(clusters, key=lambda comp: min(c for _,c in comp))
    rows = [r for r,_ in best]
    cols = [c for _,c in best]
    rmin,rmax = min(rows), max(rows)
    cmin,cmax = min(cols), max(cols)
    # find stripe rows (contiguous run of 4 of color4)
    stripe_rows = []
    for r in range(rmin, rmax+1):
        run = 0
        best_run = 0
        for c in range(cmin, cmax+1):
            if grid[r][c]==4:
                run += 1
                best_run = max(best_run, run)
            else:
                run = 0
        if best_run >= 3:
            stripe_rows.append(r)
    # fallback: if none, pick mid, top, bottom
    if not stripe_rows:
        stripe_rows = [rmin, (rmin+rmax)//2, rmax]
    stripe_rows.sort()
    H = len(stripe_rows)
    W = cmax - cmin + 1
    out = [[0]*W for _ in range(H)]
    for i,r in enumerate(stripe_rows):
        # stripe run
        run=0; segs=[]
        for c in range(cmin, cmax+1):
            if grid[r][c]==4:
                run+=1
            else:
                if run>=3: segs.append((c-run, c-1))
                run=0
        if run>=3: segs.append((cmax-run+1, cmax))
        # interior runs
        run=0; runs2=[]
        for c in range(cmin, cmax+1):
            if grid[r][c]!=0 and grid[r][c]!=4:
                run+=1
            else:
                if run>=2: runs2.append((c-run, c-1))
                run=0
        if run>=2: runs2.append((c-run, c-1))
        # mark
        for a,b in segs:
            out[i][0]=8; out[i][W-1]=8
        for a,b in runs2:
            out[i][a-cmin]=8; out[i][b-cmin]=8
    return out