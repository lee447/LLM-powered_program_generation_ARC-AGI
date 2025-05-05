def solve(grid):
    R=len(grid); C=len(grid[0])
    # find top-left block origin
    r0=0
    for i in range(R):
        if any(grid[i][j]!=0 for j in range(C)):
            r0=i
            break
    c0=0
    for j in range(C):
        if grid[r0][j]!=0:
            c0=j
            break
    # find width w and height h of block
    w=0
    while c0+w<C and grid[r0][c0+w]!=0:
        w+=1
    h=0
    while r0+h<R and grid[r0+h][c0]!=0:
        h+=1
    # extract P
    P=[grid[r0+i][c0:c0+w] for i in range(h)]
    # pattern transforms
    def mirror_h(P): return [row[::-1] for row in P]
    def mirror_v(P): return P[::-1]
    def rot180(P): return [row[::-1] for row in P[::-1]]
    fns=[lambda x:x, mirror_h, mirror_v, rot180]
    # get TL unique colors
    uvals=set()
    for row in P:
        for v in row:
            if v!=0:
                uvals.add(v)
    # prepare output
    out=[[0]*C for _ in range(R)]
    # for each quadrant
    for qi,(dr,dc) in enumerate([(0,0),(0,w),(h,0),(h,w)]):
        # build pattern_SRC
        f=fns[qi]
        pat=f(P)
        # collect seeds in region
        mapping={}
        # region rows r0+dr..r0+dr+h-1, cols c0+dc..c0+dc+w-1
        for i in range(h):
            for j in range(w):
                gr= r0+dr+i
                gc= c0+dc+j
                if 0<=gr<R and 0<=gc<C:
                    v=grid[gr][gc]
                    if v!=0:
                        t=pat[i][j]
                        mapping[t]=v
        # fill missing mapping keys
        for t in uvals:
            if t not in mapping:
                mapping[t]=0
        # write out
        for i in range(h):
            for j in range(w):
                out[r0+dr+i][c0+dc+j]=mapping[pat[i][j]]
    return out