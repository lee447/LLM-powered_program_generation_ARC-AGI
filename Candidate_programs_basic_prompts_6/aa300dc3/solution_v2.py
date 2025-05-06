def solve(grid):
    H=len(grid); W=len(grid[0])
    best_len=0; best_diag=[]
    for dr,dc in ((1,1),(1,-1)):
        for r in range(H):
            for c in range(W):
                if grid[r][c]==0:
                    pr,pc=r-dr,c-dc
                    if not (0<=pr<H and 0<=pc<W and grid[pr][pc]==0):
                        cr,cc=r,c; diag=[]
                        while 0<=cr<H and 0<=cc<W and grid[cr][cc]==0:
                            diag.append((cr,cc))
                            cr+=dr; cc+=dc
                        if len(diag)>best_len:
                            best_len=len(diag); best_diag=diag
    res=[row[:] for row in grid]
    for r,c in best_diag:
        res[r][c]=8
    return res