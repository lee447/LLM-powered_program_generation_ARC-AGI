from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    pts = [(r,c) for r in range(h) for c in range(w) if grid[r][c]==8]
    # find bar: longest horizontal run
    best = (0,0,0)
    for r in range(h):
        c=0
        while c<w:
            if grid[r][c]==8:
                s=c
                while c<w and grid[r][c]==8: c+=1
                if c-s>best[0]: best=(c-s,r,s)
            else: c+=1
    L, br, bc = best
    # find pivot on bar where trunk attaches
    pivot = None
    for j in range(bc,bc+L):
        for dr in (-1,1):
            rr,cc = br+dr,j
            if 0<=rr<h and grid[rr][cc]==8:
                pivot=(br,j); tdir=(dr,0)
                break
        if pivot: break
    pr,pc = pivot
    # collect shape coords relative to pivot
    shape = []
    for r,c in pts:
        shape.append((r-pr,c-pc))
    # detect free counts in each dir
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    bestd = ( -1,(1,0) )
    for d in dirs:
        cnt = float('inf')
        for dr,dc in shape:
            rr,cc = pr+dr, pc+dc
            step=0
            while True:
                rr+=d[0]; cc+=d[1]
                if not(0<=rr<h and 0<=cc<w and grid[rr][cc]==0): break
                step+=1
            cnt = min(cnt,step)
        if cnt>bestd[0]: bestd=(cnt,d)
    steps, ndir = bestd
    # rotation: map tdir->ndir via k times CCW
    def rot(dr,dc):
        return -dc,dr
    k=0; td=tdir
    while td!=ndir and k<4:
        td=rot(*td); k+=1
    # remove original
    for r,c in pts: grid[r][c]=0
    # place moved shape
    for dr,dc in shape:
        rr,cc = pr+dr, pc+dc
        for _ in range(steps):
            rr+=ndir[0]; cc+=ndir[1]
        # rotate around new pivot
        x,y = rr-pr, cc-pc
        for _ in range(k):
            x,y = -y,x
        r2,c2 = pr+x, pc+y
        if 0<=r2<h and 0<=c2<w:
            grid[r2][c2]=8
    return grid