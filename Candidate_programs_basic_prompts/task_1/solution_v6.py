def solve(grid):
    H = len(grid)
    W = len(grid[0])
    out = [[0]*W for _ in range(H)]
    def find_pure_row():
        for r in range(H):
            vals = set(grid[r]) - {0}
            if len(vals)==1:
                v = vals.pop()
                segs = []
                c = 0
                while c<W:
                    if grid[r][c]==v:
                        s=c
                        while c<W and grid[r][c]==v: c+=1
                        if c-s>=2: segs.append((s,c-1))
                    else:
                        c+=1
                if segs:
                    return r,v,segs
        return None
    pu = find_pure_row()
    if pu:
        r0,v,segs0 = pu
        widths = [e-s+1 for (s,e) in segs0]
        wmin = min(widths)
        segs = [(s,s+wmin-1) for (s,_) in segs0]
        # find block period
        r1 = None
        for r in range(r0+1,H):
            cnt = sum(grid[r][c]==v for (s,e) in segs for c in range(s,e+1))
            if cnt>=len(segs)*wmin:
                r1 = r
                break
        if r1 is None:
            period = H
        else:
            period = r1 - r0
        # copy pure rows and 4 rows below if present
        for b in range(0,H,period):
            rb = r0+b
            if rb>=H: break
            for (s,e) in segs:
                for c in range(s,e+1):
                    out[rb][c] = v
                # copy below 4 rows of pattern
                for d in range(1,5):
                    r2 = rb+d
                    if r2< H:
                        for c in range(s,e+1):
                            if grid[r2][c]!=0:
                                out[r2][c] = grid[r2][c]
    return out