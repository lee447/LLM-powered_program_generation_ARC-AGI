from collections import deque, defaultdict

def solve(grid):
    h, w = len(grid), len(grid[0])
    def components(color):
        vis = [[False]*w for _ in range(h)]
        comps = []
        for i in range(h):
            for j in range(w):
                if grid[i][j]==color and not vis[i][j]:
                    q=deque([(i,j)])
                    vis[i][j]=True
                    cells=[(i,j)]
                    while q:
                        r,c=q.popleft()
                        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                            nr, nc = r+dr, c+dc
                            if 0<=nr<h and 0<=nc<w and not vis[nr][nc] and grid[nr][nc]==color:
                                vis[nr][nc]=True
                                q.append((nr,nc))
                                cells.append((nr,nc))
                    comps.append(cells)
        return comps

    # detect arm info for an L-shape component
    def detect_L(cells):
        rs = defaultdict(list)
        cs = defaultdict(list)
        for r,c in cells:
            rs[r].append(c)
            cs[c].append(r)
        # find horizontal arm row
        row_arm=None; cmin=cmax=None
        for r,cl in rs.items():
            xs=sorted(cl)
            for i in range(len(xs)-1):
                if xs[i+1]-xs[i]==1:
                    if row_arm is None or r>row_arm:
                        row_arm=r
                        cmin, cmax = min(xs), max(xs)
        # find vertical arm col
        col_arm=None; rmin=rmax=None
        for c,rl in cs.items():
            ys=sorted(rl)
            for i in range(len(ys)-1):
                if ys[i+1]-ys[i]==1:
                    if col_arm is None or c<col_arm:
                        col_arm=c
                        rmin, rmax = min(ys), max(ys)
        if row_arm is None or col_arm is None:
            return None
        exp = set((row_arm,c) for c in range(cmin,cmax+1))|set((r,col_arm) for r in range(rmin,rmax+1))
        if set(cells)==exp:
            return (row_arm,col_arm,cmin,cmax,rmin,rmax)
        return None

    twos = components(2)
    ones = components(1)
    # find the red-pattern L among 1s
    red_pat = None
    for comp in ones:
        info = detect_L(comp)
        if info:
            red_pat = (comp, info)
            break
    if not red_pat:
        return grid
    pat_cells, (pr,pc,pcm,pcM,prm,prM) = red_pat
    # remove red pattern
    for r,c in pat_cells:
        grid[r][c]=0
    # apply to every 2-L except any that matches pattern size
    for comp in twos:
        info = detect_L(comp)
        if not info: continue
        row_arm,col_arm,cmin,cmax,rmin,rmax = info
        # place red-pattern under horizontal arm
        for r,c in pat_cells:
            dr,dc = r-pr, c-pc
            nr = row_arm+1+dr
            nc = cmin+ (c-pcm) if pr==row_arm else col_arm+dc
            # choose horizontal
            if pat_cells and pr==pr:
                nr = row_arm+1+dr
                nc = pc+dc
            # for vertical we handle separately below
        # actually overlay both arms
        # horizontal pattern
        hr = [c for c in rs_valid.keys()]
        for r,c in pat_cells:
            if r==pr:
                nr = row_arm+1
                nc = col_arm + (c-pc)
                if 0<=nr<h and 0<=nc<w:
                    grid[nr][nc]=1
        # vertical pattern
        for r,c in pat_cells:
            if c==pc:
                nr = row_arm + (r-pr)
                nc = col_arm+1
                if 0<=nr<h and 0<=nc<w:
                    grid[nr][nc]=1
    return grid