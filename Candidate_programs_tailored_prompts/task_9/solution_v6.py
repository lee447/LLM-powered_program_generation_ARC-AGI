def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [[0]*w for _ in range(h)]
    gs = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c]==5:
                gs.add((r,c))
                res[r][c]=5
    visited = set()
    def neighbors(r,c):
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            yield r+dr,c+dc
    frames = []
    for cell in gs:
        if cell in visited: continue
        stack = [cell]
        comp = set()
        while stack:
            u = stack.pop()
            if u in comp: continue
            comp.add(u)
            for v in neighbors(*u):
                if v in gs and v not in comp:
                    stack.append(v)
        visited |= comp
        rs = [r for r,c in comp]
        cs = [c for r,c in comp]
        minr, maxr = min(rs), max(rs)
        minc, maxc = min(cs), max(cs)
        frames.append((comp,minr,maxr,minc,maxc))
    for comp,minr,maxr,minc,maxc in frames:
        # orientation
        width = maxc-minc+1
        height = maxr-minr+1
        if all((maxr,c) in comp for c in range(minc,maxc+1)):
            # upright
            stripe_r = minr-1
        else:
            stripe_r = maxr+1
        # find leg columns
        leg_cols = sorted(c for r,c in comp if (stripe_r>minr and stripe_r<maxr) or True
                          if any((rr,c) in comp for rr in (minr,maxr)))
        leg_cols = []
        for c in range(minc,maxc+1):
            col_cells = [ (r,c) for r in range(minr,maxr+1) ]
            if sum((r,c) in comp for r,c in col_cells)==height:
                # full column border => leg
                if (minr,c) in comp or (maxr,c) in comp:
                    leg_cols.append(c)
        if len(leg_cols)>=2:
            lc, rc = min(leg_cols), max(leg_cols)
        else:
            lc, rc = minc, maxc
        for c in range(lc+1,rc):
            if 0<=stripe_r<h:
                res[stripe_r][c]=2
        # center fill if square 4x4
        if width==4 and height==4:
            for r in (minr+1,minr+2):
                for c in (minc+1,minc+2):
                    res[r][c]=2
    return res