def solve(grid):
    h,w=len(grid),len(grid[0])
    # find the 4x4 grey block
    r0=r1=c0=c1=None
    for i in range(h):
        for j in range(w):
            if grid[i][j]==5:
                if r0 is None or i<r0: r0=i
                if r1 is None or i>r1: r1=i
                if c0 is None or j<c0: c0=j
                if c1 is None or j>c1: c1=j
    # block rows r0..r1, cols c0..c1
    blocks=[]
    for (sr,sc) in [(0,0),(0,c1+1),(r1+1,0),(r1+1,c1+1)]:
        er = r0-1 if sr<r0 else h-1
        ec = c0-1 if sc<c0 else w-1
        Q=[row[sc:ec+1] for row in grid[sr:er+1]]
        H,W=len(Q),len(Q[0])
        # find minimal tile
        for th in range(1,H+1):
            if H%th: continue
            for tw in range(1,W+1):
                if W%tw: continue
                ok=True
                for i in range(H):
                    for j in range(W):
                        if Q[i][j]!=Q[i%th][j%tw]:
                            ok=False; break
                    if not ok: break
                if ok:
                    T=[row[:tw] for row in Q[:th]]
                    blocks.append((T,sr,sc))
                    th=H+1; break
            else: continue
            break
    # select the block whose tile has exactly two non-{7,5} colors
    def score(b):
        T=b[0]
        s=set(sum(T,[]))
        s-= {7,5}
        return len(s)==2
    for T,_,_ in blocks:
        if score((T,_,_)):
            return T
    return blocks[0][0]